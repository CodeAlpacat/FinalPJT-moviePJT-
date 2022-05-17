from enum import unique
from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    overview = models.TextField()
    poster_path = models.TextField()
    vote_average = models.FloatField()
    release_date = models.CharField(max_length=15)
    genres = models.ManyToManyField(Genre, related_name= 'movie_genres') # 장르와 영화는 NtoM 관계, 영화는 여러 장르 포함, 각 장르에 해당하는 영화 또한 여러개

#사용자가 팔로우한 영화 테이블(사용자 => 다수의 영화, 영화 => 다수의 사용자)
class MovieFollow(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_follows')
    kept_by_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='keep_movies')
