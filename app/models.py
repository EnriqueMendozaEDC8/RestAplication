from django.db import models
import datetime
# Create your models here.

class Genre(models.Model):
    name = models.TextField()
    infogenre = models.TextField()
    def __str__(self):
        return self.name
        
class Movie(models.Model):
    name = models.CharField(max_length=255)
    poster = models.URLField()
    premieredate = models.DateField(default=datetime.date.today)
    genre = models.ForeignKey(Genre,on_delete = models.CASCADE)
    def __str__(self):
        return self.name

class Actors(models.Model):
    name = models.CharField(max_length=255)
    photo = models.TextField()
    birthdate = models.DateField(default=datetime.date.today)
    def __str__(self):
        return self.name

class MovieActors(models.Model):
    movie = models.ForeignKey(Movie,on_delete = models.CASCADE)
    actor = models.ForeignKey(Actors,on_delete = models.CASCADE)