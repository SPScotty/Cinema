from rest_framework import serializers

from .models import *

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre', 'year', 'runtime', 'cast', 'uploader')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = MoviePosterSerializer(instance.images.all(), 
            many=True, context=self.context).data
        return representation


    
class MoviePosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviePoster
        fields = '__all__'

    # def _get_image_url(self, obj):
    #     if obj.poster:
    #         url = obj.poster.url
    #         request = self.context.get('request')
    #         if request is not None:
    #             url = request.build_absolute_uri(url)
    #     else:   
    #         url = ''
    #     return url

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['images'] = self._get_image_url(instance)
    #     return representation
