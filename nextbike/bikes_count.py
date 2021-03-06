import dataclasses
import urllib.error
import urllib.request
import json

COUNTRY = "cz"
CITY = "Pardubice"
FAVORITE_PLACES = (
    "Poliklinika Vektor",
    "Na Spravedlnosti - K.Ř. PČR",
    "Sokolovna - Na Olšinkách",
)
SHOW_FAVORITE_PLACES_ONLY = True

URL = f"https://api.nextbike.net/maps/nextbike-official.json?countries={COUNTRY}"

BIKE_EMOJI = "🚲"
NO_BIKE_EMOJI = "🚳"


@dataclasses.dataclass()
class Place:
    name: str
    bikes_available_to_rent: int
    is_favorite: bool


@dataclasses.dataclass()
class City:
    name: str
    available_bikes: int
    places: list[Place]


def main() -> None:
    city = get_city(get_data())
    max_name_length = max([len(p.name) for p in city.places])
    max_count_length = len(str(city.available_bikes))

    print_bikes(city.name, max_name_length, city.available_bikes, max_count_length)
    print()

    favorite_places = [p for p in city.places if p.is_favorite]
    for place in favorite_places:
        print_bikes(
            place.name, max_name_length, place.bikes_available_to_rent, max_count_length
        )

    if SHOW_FAVORITE_PLACES_ONLY:
        return

    if len(favorite_places) > 0:
        print()

    for place in [p for p in city.places if not p.is_favorite]:
        print_bikes(
            place.name, max_name_length, place.bikes_available_to_rent, max_count_length
        )


def get_data() -> dict:
    try:
        request = urllib.request.urlopen(URL)
        return json.load(request)
    except (urllib.error.HTTPError, urllib.error.URLError):
        print(f"Cannot connect to '{URL}'.")
        exit(1)


def get_city(data: dict) -> City:
    countries = data["countries"]

    if len(countries) == 0:
        print(f"Country '{COUNTRY}' not found.")
        exit(1)

    city_countries = [
        c for c in countries if c["name"].lower() == f"nextbike {CITY}".lower()
    ]

    if len(city_countries) == 0:
        print(f"Country for city '{CITY}' not found.")
        exit(1)

    cities = city_countries[0]["cities"]

    if len(cities) == 0:
        print(f"City '{CITY}' not found.")
        exit(1)

    city = cities[0]
    places = sorted(
        [
            Place(
                p["name"],
                p["bikes_available_to_rent"],
                p["name"].lower() in [f.lower() for f in FAVORITE_PLACES],
            )
            for p in city["places"]
        ],
        key=lambda p: p.name,
    )

    return City(city["name"], city["available_bikes"], places)


def print_bikes(
    name: str, max_name_length: int, count: int, max_count_lenght: int
) -> None:
    print(
        f"{name:<{max_name_length}} "
        f"{count:>{max_count_lenght}} "
        f"{BIKE_EMOJI if count > 0 else NO_BIKE_EMOJI}"
    )


if __name__ == "__main__":
    main()
