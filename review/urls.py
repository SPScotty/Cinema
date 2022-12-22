from django.urls import path

from review.views import CommentListCreateView, FavoriteListCreateView, LikeListCreateView

urlpatterns = [
    path('favorites/', FavoriteListCreateView.as_view(), name='favorite-list-create'),
    path('likes/', LikeListCreateView.as_view(), name='like-list-create'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
]
