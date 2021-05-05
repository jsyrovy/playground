from movies.database.db_session import db_session, engine
from movies.database.base import Base
from movies.models.genres import Genres
from movies.models.movies import Movies
from movies.models.actors import Actors


def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    crime = Genres(name="Crime")
    db_session.add(crime)
    drama = Genres(name="Drama")
    db_session.add(drama)
    action = Genres(name="Action")
    db_session.add(action)
    fantasy = Genres(name="Fantasy")
    db_session.add(fantasy)

    pulp_fiction = Movies(name="Pulp Fiction", director="Quentin Tarantino", genre=crime)
    db_session.add(pulp_fiction)
    meet_joe_black = Movies(name="Meet Joe Black", director="Martin Brest", genre=drama)
    db_session.add(meet_joe_black)
    guardians_of_the_galaxy = Movies(name="Guardians of the Galaxy", director="James Gunn", genre=action)
    db_session.add(guardians_of_the_galaxy)
    the_lord_of_the_rings = Movies(name="The Lord of the Rings: The Fellowship of the Ring", director="Peter Jackson", genre=fantasy)
    db_session.add(the_lord_of_the_rings)

    travolta = Actors(name="John Travolta", movie=pulp_fiction)
    db_session.add(travolta)
    jackson = Actors(name="Samuel L. Jackson", movie=pulp_fiction)
    db_session.add(jackson)
    pitt = Actors(name="Brad Pitt", movie=meet_joe_black)
    db_session.add(pitt)
    hopkins = Actors(name="Anthony Hopkins", movie=meet_joe_black)
    db_session.add(hopkins)
    pratt = Actors(name="Chris Pratt", movie=guardians_of_the_galaxy)
    db_session.add(pratt)
    diesel = Actors(name="Vin Diesel", movie=guardians_of_the_galaxy)
    db_session.add(diesel)
    wood = Actors(name="Elijah Wood", movie=the_lord_of_the_rings)
    db_session.add(wood)
    bloom = Actors(name="Orlando Bloom", movie=the_lord_of_the_rings)
    db_session.add(bloom)

    db_session.commit()
