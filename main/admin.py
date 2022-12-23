from django.contrib import admin

from .models import *



class MoviePoster(admin.TabularInline):
    model = MoviePoster
    max_num = 2
    min_num = 1


admin.site.register(Genre)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')
    inlines = [MoviePoster, ]

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie')

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'comment', 'created_at')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'value')


