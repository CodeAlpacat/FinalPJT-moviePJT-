from rest_framework import serializers
from ..models import Movie, Review
from django.contrib.auth import get_user_model

class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):

    class ReviewSerializer(serializers.ModelSerializer): # 개별 영화에 소속된 리뷰들에 대한 정보들을 가져오기 위함
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('pk', 'username')
        user = UserSerializer(read_only=True)
        like_count = serializers.IntegerField()
        class Meta:
            model = Review
            fields = ('pk', 'movie', 'content', 'liked_users', 'user', 'like_count')
    
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('title', 'overview', 'poster_path', 'vote_average', 'release_date', 'genres', 'kept_by_user', 'reviews')