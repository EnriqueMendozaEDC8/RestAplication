
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from .models import Actors,Genre,Movie,MovieActors


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'infogenre']

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['name','poster','genre']

class ActorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actors
        fields = ['name','photo','birthdate']

class MovieActorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MovieActors
        fields = ['movie','actor']