import sqlalchemy.orm

from movies.database.base import Base
from movies.models.genres import Genres


class Movies(Base):
    __tablename__ = "movies"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    director = sqlalchemy.Column(sqlalchemy.String)
    genre_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("genres.id"))
    genre = sqlalchemy.orm.relationship(
        Genres,
        backref=sqlalchemy.orm.backref("movies", uselist=True, cascade="delete,all")
    )
