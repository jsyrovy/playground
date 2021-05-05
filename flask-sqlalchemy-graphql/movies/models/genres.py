import sqlalchemy

from movies.database.base import Base


class Genres(Base):
    __tablename__ = "genres"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
