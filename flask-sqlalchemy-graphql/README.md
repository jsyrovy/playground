# flask-sqlalchemy-graphql-demo

Demo GraphQL application in Flask.

## Installation (Windows)

Create virtual env.

`py -m venv venv`

Install dependencies.

`.\venv\Scripts\python.exe -m pip install -r .\requirements.txt`

Run app.

`.\venv\Scripts\python.exe .\autoapp.py`

Open URL.

`http://127.0.0.1:5000/graphql`

## Examples

Get movies by genre.

```graphql
{
  moviesByGenre(name: "Crime") {
    name
    director
  }
}
```

Create movie.

```graphql
mutation {
  createMovie(input: {name: "Death at a Funeral", director: "Frank Oz"}) {
    movie {
      id
      name
      director
    }
  }
}
```
