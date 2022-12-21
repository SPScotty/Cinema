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
    return Response({'genres':serializer.data})


@api_view(['GET'])
def movies(request):
    movies = Movie.objects.all()
    serializer = MovieSeriailizer(movies, many=True)
    return Response({'movies':serializer.data})

@api_view(['POST'])
def post_movie(request):
    print(request.data)
    movie = request.data
    serializer = MovieSeriailizer(data=movie)
    if serializer.is_valid(raise_exception=True):
        post_saved = serializer.save()
    return Response(serializer.data)

