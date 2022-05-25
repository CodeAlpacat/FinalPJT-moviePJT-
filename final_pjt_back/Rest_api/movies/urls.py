from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('upcoming/',views.upcoming_movie_list),
    path('nowplaying/', views.nowplaying_movie_list),
    path('recommend/<int:user_pk>/', views.recommend_movie_list),
    path('genres/', views.genres_list),
    path('<int:movie_pk>/moviefollow/', views.movie_follow),
    path('<int:movie_pk>/reviews/', views.create_review),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_delete),
    path('<int:movie_pk>/reviews/<int:review_pk>/like/', views.like_review),
    path('<int:page_pk>/more/', views.more_movies),
]
