from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSeriailizer

@api_view(['GET'])
def genres(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response({f'genres':serializer.data})


class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSeriailizer(movies, many=True)
        return Response(serializer.data)