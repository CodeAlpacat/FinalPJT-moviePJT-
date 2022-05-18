from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import MovieFollow
from community.models import Article

class ProfileSerializer(serializers.Serializer):

    class ArticleSerializer(serializers.Serializer):
        
        class Meta:
            model = Article
            fields = ('pk', 'title', 'content')
    
    class MovieFollowSerializer(serializers.Serializer):
        
        class Meta:
            model = MovieFollow
            fields = ('pk', 'movie', 'kept_by_user')
        
    # 유저가 좋아요한 게시글 / 유저가 작성한 게시글
    like_articles = ArticleSerializer(many=True)
    articles = ArticleSerializer(many=True)
    kept_by_user = MovieFollowSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'like_articles', 'articles', 'kept_by_user')