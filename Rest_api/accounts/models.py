from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

#회원가입 시에 들어가는 정보가 데이터베이스에도 저장되려면 AccountAdapter을 생성하기위해 adapter.py 생성
class User(AbstractUser):
    # followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followers')
    profile_img =  ProcessedImageField(
        blank=True,
        upload_to = 'profile_img',
        processors=[ResizeToFill(300, 300)],
        format = 'PNG',
        options = {'quality': 80},
    )
    genre_likes = models.JSONField(default='{}')