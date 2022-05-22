from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Review, Movie

class ReviewSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    like_count =serializers.IntegerField(source="liked_users.count", read_only=True)
    class Meta:
        model = Review
        fields = ('pk', 'user', 'content', 'liked_users', 'user', 'movie','like_count')
        read_only_fields = ('movie','like_count')