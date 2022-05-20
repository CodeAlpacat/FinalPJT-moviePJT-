from rest_framework import serializers
from ..models import Movie

#팔로우한 영화를 보여줘야하는 페이지가 있는가?
class MovieFollowSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'