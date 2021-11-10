from django.urls import path

from movie.views import ActorViewSet, director_view, genre

urlpatterns = [
    path('genres/', genre, name='genres'),
    path('directors/', director_view, name='directors'),
    path('actors/', ActorViewSet.as_view(), name='actors')
]
