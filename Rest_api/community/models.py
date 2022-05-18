from django.db import models
from django.conf import settings



class Article(models.Model): # 작성한 리뷰
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True) # 게시글에 대한 좋아요.


class Comment(models.Model): # 작성한 리뷰
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments', blank=True) #댓글에 대한 좋아요.

