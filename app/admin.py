from django.contrib import admin
from app.models import Genre,Movie,Actors,MovieActors
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name','infogenre')
    search_fields = ('name','infogenre')

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name','poster','genre','premieredate')
    search_fields = ('name','poster','genre','premieredate')

class ActorsAdmin(admin.ModelAdmin):
    list_display = ('name','birthdate')
    search_fields = ('name','birthdate')

class MovieActorsAdmin(admin.ModelAdmin):
    list_display = ('movie','actor')
    search_fields = ('movie','actor')

admin.site.register(Genre,GenreAdmin)
admin.site.register(Movie,MovieAdmin)
admin.site.register(Actors,ActorsAdmin)
admin.site.register(MovieActors,MovieActorsAdmin)