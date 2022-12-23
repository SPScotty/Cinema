from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework import generics, viewsets, status
from django.db.models import Q
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet




from .models import Genre, Movie, MoviePoster
from .serializers import GenreSerializer, MovieSerializer, MoviePosterSerializer
from .permissions import *






def index(request):
    video=Video.objects.all()
    return render(request,"index.html",{"video":video})

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            return [IsAuthenticated()]
        return [IsAdmin()]



class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated, ]
    

    def get_serializer_context(self):
        return {'request':self.request}

    def get_permissions(self):
        '''Переопределим данный метод'''
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            permissions= [IsAuthorOrReadOnly,]
        else:
            permissions = []
        return [permission() for permission in permissions]

    @action(detail=False, methods=['get'])
    def search(self, request, px=None):
        q = request.query_params.get('q')
        queryset = self.get_queryset()
        queryser = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q)| Q(genre__slug__icontains=q))
        serializer = MovieSerializer(queryser, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK) 



class MoviePosterViewSet(ModelViewSet):
    queryset = MoviePoster.objects.all()
    serializer_class = MoviePosterSerializer
    
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            return [IsAuthenticated()]
        return [IsAdmin()]

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



