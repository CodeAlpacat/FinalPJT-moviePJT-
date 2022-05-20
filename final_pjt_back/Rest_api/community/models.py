from django.db import models
from django.conf import settings


# user을 통해 게시글을 작성한 유저 / 역참조를 통한 유저가 작성한 게시글 조회 가능
# liked_users를 통한 게시글 좋아요 및 게시글에 좋아요를 누른 유저 조회
class Article(models.Model): # 작성한 리뷰
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True) # 게시글에 대한 좋아요.


# user을 통해 댓글을 작성한 유저 / 역참조를 통한 유저가 작성한 댓글 조회 가능
# article을 통해 댓글이 게시된 게시글 / 게시글에 댓글을 단 목록 조회 가능
# liked_users를 통한 게시글 좋아요 / 역참조를 통한 게시글에 좋아요를 누른 유저 조회
class Comment(models.Model): # 작성한 리뷰
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments', blank=True) #댓글에 대한 좋아요.
