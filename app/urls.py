from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from . import views as movieView

router = routers.DefaultRouter()
router.register(r'genero',movieView.GenreViewSet)
router.register(r'actores',movieView.ActorsViewSet)
router.register(r'peliculas',movieView.MovieViewSet)
router.register(r'actoresporpelicula',movieView.MovieActorsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('hello/',movieView.hello_world),
    path('getMovieActors/',movieView.getMovieActors.as_view()),
    path('getActorMovies/',movieView.getActorMovies.as_view()),
    path('getActors/',movieView.getActors.as_view()),
    path('getMovies/',movieView.getMovies.as_view()),
]