from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Article
from ..models import Comment

#게시글 전체 조회
#게시글 좋아요 횟수 / 달린 댓글의 갯수 / 작성자
class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')
    
    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'

    user = UserSerializer(read_only=True)
    comment_count = serializers.IntegerField()
    like_count = serializers.IntegerField()

    class Meta:
        model = Article
        fields = ('pk', 'user', 'title', 'content', 'comment_count', 'like_count',  'created_at', 'updated_at')


#detail 특정 게시글 조회
#게시글에 달린 댓글들, 댓글에 달린 좋아요, 게시글 작성자, 댓글 작성자
class ArticleSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')
    
    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'

    user = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    liked_users = UserSerializer(read_only=True, many=True)
    class Meta:
        model = Article
        fields = ('pk', 'user', 'title', 'content', 'comments', 'liked_users', 'created_at', 'updated_at')
