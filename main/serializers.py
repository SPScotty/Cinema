from rest_framework import serializers

from .models import *

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSeriailizer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
    