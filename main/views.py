from django.shortcuts import render, redirect, get_object_or_404
from .models import Like, Favorite
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import redirect, get_object_or_404

from .models import Genre, Movie, MoviePoster
from .serializers import GenreSerializer, MovieSerializer

# @api_view(['GET'])
# def genres(request):
#     genres = Genre.objects.all()
#     serializer = GenreSerializer(genres, many=True)
#     return Response({'genres':serializer.data})


# @api_view(['GET'])
# def movies(request):
#     movies = Movie.objects.all()
#     serializer = MovieSerializer(movies, many=True)
#     return Response({'movies':serializer.data})

# @api_view(['POST'])
# def post_movie(request):
#     print(request.data)
#     movie = request.data
#     serializer = MovieSerializer(data=movie)
#     if serializer.is_valid(raise_exception=True):
#         post_saved = serializer.save()
#     return Response(serializer.data)

class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class MovieView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieUpdateView(generics.UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDeleteView(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# class PostImageView(generics.ListAPIView):
#     queryset = MoviePoster.objects.all()
#     serializer_class = MoviePosterSerializer

#     def get_serializer_context(self):
#         return {'request':self.request}

@api_view(['POST'])
def like_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    like, created = Like.objects.get_or_create(user=request.user, movie=movie)
    if not created:
        like.delete()
    return redirect('movies:detail', movie_id=movie_id)
@api_view(['POST'])
def add_to_favorites(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, movie=movie)
    return redirect('movies:detail', movie_id=movie_id)
