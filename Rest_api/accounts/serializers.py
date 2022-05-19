from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import MovieFollow
from community.models import Article
from dj_rest_auth.registration.serializers import RegisterSerializer

class ProfileSerializer(serializers.Serializer):
    
    #유저가 좋아요한 게시글들, 유저가 작성한 게시글을 가져오기 위해 재정의
    class ArticleSerializer(serializers.Serializer):
        
        class Meta:
            model = Article
            fields = ('pk', 'title', 'content')

    #유저가 팔로우한 영화들을 가져오기 위해 재정의
    class MovieFollowSerializer(serializers.Serializer):
        
        class Meta:
            model = MovieFollow
            fields = ('pk', 'movie')
        
    # 유저가 좋아요한 게시글 / 유저가 작성한 게시글 / 유저가 팔로우한 영화들
    like_articles = ArticleSerializer(many=True)
    articles = ArticleSerializer(many=True)
    keep_movies = MovieFollowSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'like_articles', 'articles', 'keep_movies')

class CustomSignupSerializer(RegisterSerializer):
    # profile_img = serializers.ImageField(use_url=True)
    genre_likes = serializers.JSONField(default='{}')
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        # data['profile_img'] = self.validated_data.get('profile_img', '')
        data['genre_likes'] = self.validated_data.get('genre_likes', '')

        return data