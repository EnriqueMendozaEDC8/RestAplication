from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from app.serializers import GenreSerializer,ActorsSerializer,MovieSerializer,MovieActorsSerializer
from app.models import Genre,Actors,Movie,MovieActors
import json

# Create your views here.
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class ActorsViewSet(viewsets.ModelViewSet):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer
    
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class MovieActorsViewSet(viewsets.ModelViewSet):
    queryset = MovieActors.objects.all()
    serializer_class = MovieActorsSerializer

class getActorsMovie(APIView):
    def get(self,request):
        return Response("este es un metodo post")
    def post(self,request):
        try:
            movieToFind = request.data["name"]
            queryset = Movie.objects.filter(name=movieToFind)
            queryset = MovieActors.objects.filter(movie=queryset[0].id)
            response = []
            for data in queryset:
                response.append({"movie":data.movie.name,"actor":data.actor.name})
            return Response({"data":response})
        except:
            return Response({"data":{"menssage":"Los datos enviados son incorrectos","request":request.data}})

class getActors(APIView):
    def get(self,request):
        return Response("this is my menssage")
    def post(self,request):
        try:
            if existParam(request.data,'name'):
                queryset = Actors.objects.filter(name = request.data["name"]).values('name','photo','birthdate')
            else:
                queryset = Actors.objects.all().values('name','photo','birthdate')  
            return Response({"data":list(queryset)})
        except:
            return Response({"data":{"menssage":"Los datos enviados son incorrectos","request":request.data}})
            
class getActors(APIView):
    def get(self,request):
        return Response("this is my menssage")
    def post(self,request):
        try:
            if existParam(request.data,'name'):
                queryset = Actors.objects.filter(name = request.data["name"]).values('name','photo','birthdate')
            else:
                queryset = Actors.objects.all().values('name','photo','birthdate')  
            return Response({"data":list(queryset)})
        except:
            return Response({"data":{"menssage":"Los datos enviados son incorrectos","request":request.data}})

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

def existParam(var,find):
    try:
        var[find]=var[find]
        return True
    except:
        return False