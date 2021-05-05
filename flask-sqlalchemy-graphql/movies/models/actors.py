import sqlalchemy.orm

from movies.database.base import Base
from movies.models.movies import Movies


class Actors(Base):
    __tablename__ = "actors"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    movie_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("movies.id"))
    movie = sqlalchemy.orm.relationship(
        Movies,
        backref=sqlalchemy.orm.backref("actors", uselist=True, cascade="delete,all")
    )
