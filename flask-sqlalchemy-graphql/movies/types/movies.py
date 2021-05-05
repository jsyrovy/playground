import graphene
import graphene_sqlalchemy

from movies.models.movies import Movies as MoviesModel


class Movies(graphene_sqlalchemy.SQLAlchemyObjectType):
    class Meta:
        model = MoviesModel
        interfaces = (graphene.relay.Node,)


class MovieAttribute:
    name = graphene.String()
    director = graphene.String()


class CreateMovieInput(graphene.InputObjectType, MovieAttribute):
    pass
