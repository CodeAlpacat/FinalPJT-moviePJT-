# Generated by Django 3.2.12 on 2022-05-19 07:36

from django.conf import settings
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20220519_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followings',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_img',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='profile_img'),
        ),
    ]
