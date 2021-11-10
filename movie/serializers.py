from django.db import connection
from rest_framework import serializers

from movie.models import Actor


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class ActorSerializer(serializers.ModelSerializer):

    movies_count = serializers.SerializerMethodField()
    best_genre = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ('name', 'movies_count', 'best_genre')

    def get_movies_count(self, obj):
        cursor = connection.cursor()
        count_movie = cursor.execute(
            '''SELECT COUNT(movies.id)
             count_movie FROM actors, movie_actors,
             movies WHERE movie_actors.actor_id == actors.id
             AND movie_actors.movie_id == movies.id AND
             actors.name == "{}"
             GROUP BY actors.id'''.format(obj.name)
        ).fetchone()
        return count_movie[0]

    def get_best_genre(self, obj):
        cursor = connection.cursor()
        best_genre = cursor.execute(
            '''select movies.genre FROM actors, movie_actors,
             movies WHERE movie_actors.actor_id == actors.id
             AND movie_actors.movie_id == movies.id AND
             actors.name ="{}" group by movies.title
             order by - avg(movies.imdb_rating)
            '''.format(obj.name)
        ).fetchone()
        return best_genre[0]


class GenreSerializer(serializers.Serializer):

    genre = serializers.CharField()
    movies_count = serializers.IntegerField()
    avg_rating = serializers.DecimalField(max_digits=2, decimal_places=1)


class DirectorSerializer(serializers.Serializer):

    director_name = serializers.CharField()
    favourite_actors = serializers.ListField()
    best_movies = serializers.ListField()
