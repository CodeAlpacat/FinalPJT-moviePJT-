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

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews') # 영화에 대한 리뷰
    content = models.TextField() # 리뷰 내용
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews', blank=True) # 리뷰에 대한 좋아요.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews') # 리뷰 작성자