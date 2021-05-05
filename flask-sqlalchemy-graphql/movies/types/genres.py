import graphene
import graphene_sqlalchemy

from movies.models.genres import Genres as GenresModel


class Genres(graphene_sqlalchemy.SQLAlchemyObjectType):
    class Meta:
        model = GenresModel
        interfaces = (graphene.relay.Node,)