import sqlalchemy.ext.declarative

from movies.database.db_session import db_session

Base = sqlalchemy.ext.declarative.declarative_base()
Base.query = db_session.query_property()
