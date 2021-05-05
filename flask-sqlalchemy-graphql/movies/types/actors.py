import graphene
import graphene_sqlalchemy

from movies.models.actors import Actors as ActorsModel


class Actors(graphene_sqlalchemy.SQLAlchemyObjectType):
    class Meta:
        model = ActorsModel
        interfaces = (graphene.relay.Node,)
