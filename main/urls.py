from django.urls import path

from main import views



urlpatterns = [
    path('genres/', views.genres, name='genres-list'),
    path('posts/', views.MovieListView.as_view(), name='movies-list'),
]