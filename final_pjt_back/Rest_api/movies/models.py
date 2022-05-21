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
    kept_by_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='keep_movies', blank=True)

