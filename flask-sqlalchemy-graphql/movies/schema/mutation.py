import graphene

from movies.database.db_session import db_session
from movies.models.movies import Movies as MoviesModel
from movies.types.movies import Movies, CreateMovieInput
from movies.utils.input_to_dictionary import input_to_dictionary


class CreateMovie(graphene.Mutation):
    movie = graphene.Field(lambda: Movies)
    ok = graphene.Boolean()

    class Arguments:
        input = CreateMovieInput(required=True)

    @staticmethod
    def mutate(self, info, input):
        data = input_to_dictionary(input)
        movie = MoviesModel(**data)
        db_session.add(movie)
        db_session.commit()
        ok = True
        return CreateMovie(movie=movie, ok=ok)


class Mutation(graphene.ObjectType):
    createMovie = CreateMovie.Field()
