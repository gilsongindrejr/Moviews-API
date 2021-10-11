from rest_framework import serializers

from .models import Movie, Rating


class MovieSerializer(serializers.ModelSerializer):

    ratings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('name', 'release_date', 'director', 'ratings')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('user', 'movie', 'title', 'rating', 'comment')
