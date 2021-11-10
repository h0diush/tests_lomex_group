from django.db import models


class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actors'


class MovieActor(models.Model):
    movie_id = models.TextField(blank=True, null=True)
    actor_id = models.TextField(blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'movie_actors'


class Movie(models.Model):
    id = models.TextField(primary_key=True)
    genre = models.TextField(blank=True, null=True)
    director = models.TextField(blank=True, null=True)
    writer = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    imdb_rating = models.TextField(blank=True, null=True)
    writers = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'


class RatingAgency(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating_agency'


class Writer(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'writers'
