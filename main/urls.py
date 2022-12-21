from django.urls import path

from main import views



urlpatterns = [
    path('genres/', views.genres, name='genres-list'),
    path('movies/', views.movies, name='movies-list'),
    path('post_movie/', views.post_movie, name='post-movie'),
]