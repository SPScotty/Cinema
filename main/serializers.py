from rest_framework import serializers

from .models import *

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'genre', 'year', 'runtime', 'cast')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = MoviePosterSerializer(instance.images.all(), 
            many=True, context=self.context).data,
        representation['video'] = VideoSerializer(instance.videos.all(), many = True, context=self.context).data
        
        return representation

    def create(self, validated_data):
        request = self.context.get('request')
        user_id = request.user.id
        validated_data['uploader_id'] = user_id
        movie = Movie.objects.create(**validated_data)
        return movie





    
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
