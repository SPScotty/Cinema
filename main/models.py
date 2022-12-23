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

    @property
    def average_rating(self):
        ratings = self.ratings.all()
        values = []
        for rating in ratings:
            values.append(rating.value)
        if values:
            return sum(values) / len(values)
        return 0

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['id']

class MoviePoster(models.Model):
    poster = models.ImageField(upload_to='movies', blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='images')

class Rating(models.Model):
    user = models.ForeignKey(MyUser, related_name='ratings', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,related_name='ratings', on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5),(6,6), (7,7), (8,8), (9,9), (10,10)])

    def __str__(self):
        return f'{self.user} -> {self.movie}'


class Like(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,related_name='like')
    
    def __str__(self):
        return f'{self.user} -> {self.movie}'


class Favorite(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,related_name='favorite')

    def __str__(self):
        return f'{self.user} -> {self.movie}'


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,related_name='comment')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} -> {self.movie}'