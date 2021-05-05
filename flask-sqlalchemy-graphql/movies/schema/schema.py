import graphene

from movies.schema.query import Query
from movies.schema.mutation import Mutation

from movies.types.genres import Genres
from movies.types.movies import Movies
from movies.types.actors import Actors

schema = graphene.Schema(query=Query, mutation=Mutation, types=[Genres, Movies, Actors])
