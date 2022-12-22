from django.db import models

from account.models import MyUser
from main.models import Movie

class Favorite(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    movie= models.ForeignKey(Movie, on_delete=models.CASCADE)

class Like(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    movie= models.ForeignKey(Movie, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    movie= models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.TextField()
