from rest_framework import serializers
from ..models import Genre


class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'