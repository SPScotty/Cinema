from rest_framework import serializers

from .models import *

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = MoviePosterSerializer(instance.images.all(), 
            many=True, context=self.context).data,
        representation['comment'] = CommentSerializer(instance.comment.all(), 
            many=True, context=self.context).data
        representation['favorite'] = FavoriteSerializer(instance.favorite.all(), 
            many=True, context=self.context).data
        representation['like'] = instance.like.count()
        representation['rating'] = instance.average_rating

        return representation

    def create(self, validated_data):
        request = self.context.get('request')
        user_id = request.user.id
        validated_data['uploader_id'] = user_id
        movie = Movie.objects.create(**validated_data)
        return movie


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        exclude = ('user',)

    def validate(self, attrs):
        attrs =  super().validate(attrs)
        request = self.context.get('request')
        attrs['user'] = request.user

        return attrs
        

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        exclude = ('user',)

    def validate(self, attrs):
        attrs =  super().validate(attrs)
        request = self.context.get('request')
        attrs['user'] = request.user

        return attrs

   

        

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('user',)

    def validate(self, attrs):
        attrs =  super().validate(attrs)
        request = self.context.get('request')
        attrs['user'] = request.user

        return attrs
        
        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        exclude = ('user',)

    def validate(self, attrs):
        attrs =  super().validate(attrs)
        request = self.context.get('request')
        attrs['user'] = request.user

        return attrs
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        del rep['movie']
        rep['user'] = instance.author.email
        return rep
    


    
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
