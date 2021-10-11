from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer


class MoviesViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    @action(detail=True, methods=['get'])
    def ratings(self, request, pk=None):
        movie = self.get_object()
        serializer = RatingSerializer(movie.ratings.all(), many=True)
        return Response(serializer.data)


class RatingsViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
