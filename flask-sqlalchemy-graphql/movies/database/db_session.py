import sqlalchemy.orm

engine = sqlalchemy.create_engine("sqlite:///movies/database/database.sqlite3", convert_unicode=True)
db_session = sqlalchemy.orm.scoped_session(
    sqlalchemy.orm.sessionmaker(autocommit=False, autoflush=False, bind=engine))
