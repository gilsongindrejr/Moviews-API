from django.contrib import admin

from .models import Movie, Rating


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'release_date')
    list_filter = ('director', 'release_date')
    search_fields = ('name', 'director', 'release_date')
    ordering = ('name',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'rating', 'movie')
    list_filter = ('movie', 'rating')
    search_fields = ('user', 'title', 'rating', 'movie', 'comment')
    ordering = ('movie',)
    raw_id_fields = ('user', 'movie')
