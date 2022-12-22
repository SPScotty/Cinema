from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets, status
from django.db.models import Q
from django.shortcuts import render



from .models import Genre, Movie, MoviePoster, Video
from .serializers import GenreSerializer, MovieSerializer, MoviePosterSerializer, VideoSerializer





def index(request):
    video=Video.objects.all()
    return render(request,"index.html",{"video":video})


class VideoViewSet(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=False, methods=['get'])
    def search(self, request, px=None):
        q = request.query_params.get('q')
        queryset = self.get_queryset()
        queryser = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q))
        serializer = MovieSerializer(queryser, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK) 


class PosterViewSet(generics.ListCreateAPIView):
    queryset = MoviePoster.objects.all()
    serializer_class = MoviePosterSerializer

    def get_serializer_context(self):
        return {'request':self.request}

# class MovieView(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

# class MovieDetailView(generics.RetrieveAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

# class MovieUpdateView(generics.UpdateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

# class MovieDeleteView(generics.DestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

# @api_view(['POST'])
# def post_movie(request):
#     print(request.data)
#     movie = request.data
#     serializer = MovieSerializer(data=movie)
#     if serializer.is_valid(raise_exception=True):
#         post_saved = serializer.save()
#     return Response(serializer.data)



