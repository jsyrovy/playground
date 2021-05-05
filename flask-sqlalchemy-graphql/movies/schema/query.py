import graphene

from movies.models.genres import Genres as GenresModel
from movies.models.movies import Movies as MoviesModel
from movies.types.movies import Movies


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()

    movies = graphene.List(Movies)
    movies_by_name = graphene.List(Movies, name=graphene.String())
    movies_by_genre = graphene.List(Movies, name=graphene.String())

    @staticmethod
    def resolve_movies(parent, info, **args):
        movies_query = Movies.get_query(info)

        return movies_query.all()

    @staticmethod
    def resolve_movies_by_name(parent, info, **args):
        q = args.get("name")

        movies_query = Movies.get_query(info)

        return movies_query.filter(MoviesModel.name.contains(q)).all()

    @staticmethod
    def resolve_movies_by_genre(parent, info, **args):
        q = args.get("name")

        movies_query = Movies.get_query(info)

        return movies_query.join(GenresModel).filter(GenresModel.name == q).all()
