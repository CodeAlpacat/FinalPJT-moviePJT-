from enum import unique
from django.db import models
from django.conf import settings

# Create your models here.

class GenresName(models.Model):
    name = models.CharField(max_length=50)

class Actor(models.Model):
    name = models.CharField(max_length=30)

class Movie(models.Model):
    kept_by_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='keeping_movie')
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    overview = models.TextField()
    poster_path = models.TextField()
    vote_average = models.FloatField()
    release_date = models.CharField(max_length=15)
    trailer_url = models.TextField()
    genres = models.ManyToManyField(GenresName) # 장르와 영화는 MtoM 관계, 영화는 여러 장르 포함, 각 장르에 해당하는 영화 또한 여러개
    actors = models.ManyToManyField(Actor) # 배우또한 장르와 마찬가지.


class Review(models.Model): # 작성한 리뷰
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')