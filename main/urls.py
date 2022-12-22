from django.urls import path

from main import views



urlpatterns = [
    path('genres/', views.GenreListView.as_view(), name='genres-list'),
    path('movies/', views.MovieView.as_view(), name='movies-list'),
    path('movies-detail/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('movies-update/<int:pk>/', views.MovieUpdateView.as_view(), name='movie-update'),
    path('movies-delete/<int:pk>/', views.MovieDeleteView.as_view(), name='movie-delete'),
    # path('movies/<int:movie_id>/like/', views.like_movie, name='like'),
    # path('movies/<int:movie_id>/favorite/', views.add_to_favorites, name='favorite'),
]

from django.conf import settings
from django.conf.urls.static import static


urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)