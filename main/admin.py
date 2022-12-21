from django.contrib import admin

from .models import MoviePoster, Movie, Genre

class MoviePoster(admin.TabularInline):
    model = MoviePoster
    max_num = 5
    min_num = 1

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [MoviePoster, ]

admin.site.register(Genre)


