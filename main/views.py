from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework import generics, viewsets, status
from django.db.models import Q
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404





from .models import *
from .serializers import *
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
            permissions = [IsAuthorOrReadOnly,]
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



class LikeViewSet(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(request_body=LikeSerializer())
    def post(self, request):
        user = request.user
        ser = LikeSerializer(data=request.data, context={"request":request})
        ser.is_valid(raise_exception=True)
        movie_id = request.data.get("movie")
        if Like.objects.filter(user=user, movie__id=movie_id).exists():
            raiting = Like.objects.get(user=user, movie__id=movie_id)
            raiting.value = request.data.get("value")
            raiting.save()
        else:
            ser.save()
        return Response(status=201)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

class RatingViewSet(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(request_body=RatingSerializer())
    def post(self, request):
        user = request.user
        ser = RatingSerializer(data=request.data, context={"request":request})
        ser.is_valid(raise_exception=True)
        movie_id = request.data.get("movie")
        if Rating.objects.filter(user=user, movie__id=movie_id).exists():
            raiting = Rating.objects.get(user=user, movie__id=movie_id)
            raiting.value = request.data.get("value")
            raiting.save()
        else:
            ser.save()
        return Response(status=201)


@api_view(['POST'])
def favourite(request):
    user_id = request.data.get('user')
    movie_id = request.data.get('movie')
    user = get_object_or_404(MyUser, id = user_id)
    movie = get_object_or_404(Movie, id = movie_id)

    if Favorite.objects.filter(movie=movie, user=user).exists():
        Favorite.objects.filter(movie=movie,user=user).delete()
    else:
        Favorite.objects.create(movie=movie,user=user)
    return Response(status=201)
