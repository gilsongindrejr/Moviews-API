from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'release_date')
    list_filter = ('director', 'release_date')
    search_fields = ('name', 'director', 'release_date')
    ordering = ('name',)
