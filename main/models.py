from django.db import models

from account.models import MyUser

class Genre(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True)
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    uploader = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='uploader')
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    genre = models.ForeignKey(Genre, related_name='movies', on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    runtime = models.PositiveIntegerField()
    cast = models.TextField()
    video = models.FileField(upload_to='trailers', null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['id']

class MoviePoster(models.Model):
    poster = models.ImageField(upload_to='movies', blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='images')


    
