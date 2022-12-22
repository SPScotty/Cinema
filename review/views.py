from rest_framework import generics
from review.models import Favorite, Like, Comment

from review.serializers import CommentSerializer, FavoriteSerializer, LikeSerializer

class FavoriteListCreateView(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

