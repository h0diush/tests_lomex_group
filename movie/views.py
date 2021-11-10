from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from movie.models import Actor
from movie.serializers import (ActorSerializer, DirectorSerializer,
                               GenreSerializer)
from movie.utilits import get_genre


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class ActorViewSet(ListAPIView):
    serializer_class = ActorSerializer

    def get_queryset(self):
        return Actor.objects.all()[:20]


@api_view(['GET'])
def genre(request):
    data = []
    cursor = connection.cursor()
    all_genre = cursor.execute(
        '''select genre from movies limit 20'''
    ).fetchall()
    test = get_genre(all_genre)
    test.pop()
    for genre in test:
        if genre == '':
            continue
        else:
            count_movie = cursor.execute(
                f'''SELECT COUNT(id) AS count,
                AVG(imdb_rating)_movie FROM movies
                WHERE genre LIKE '%{genre}%' ''',
            ).fetchone()
            data.append(
                {
                    'genre': genre,
                    'movies_count': count_movie[0],
                    'avg_rating': round(count_movie[1], 1)
                }
            )
    serializer = GenreSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def director_view(request):
    data = []
    cursor = connection.cursor()
    directors = cursor.execute(
        '''SELECT distinct director from movies limit 20'''
    ).fetchall()
    for director in directors:
        movies = cursor.execute(
            '''select title as best_movies
            from movies where director = "{}"
            order by - imdb_rating limit 3'''.format(director[0])).fetchall()

        res_list = cursor.execute(
            '''select actors.name, count(movies.title) as movie_count
            from movies,actors, movie_actors where
            movies.id = movie_actors.movie_id AND
            actors.id = movie_actors.actor_id
            AND director = "{}" group by actors.name
            order by - avg(movies.imdb_rating) and -count(movies.title)
            limit 3'''.format(director[0])
        )
        data.append(
            {
                'director_name': director[0],
                'favourite_actors': dictfetchall(res_list),
                'best_movies': movies
            }
        )
    # print(director)
    serializer = DirectorSerializer(data, many=True)
    return Response(serializer.data)
