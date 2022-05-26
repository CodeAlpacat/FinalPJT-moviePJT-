from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('upcoming/',views.upcoming_movie_list), # 개봉 예정
    path('nowplaying/', views.nowplaying_movie_list), # 현재 상영중
    path('recommend/<int:user_pk>/', views.recommend_movie_list), # 추천 영화
    path('genres/', views.genres_list),
    path('<int:movie_pk>/moviefollow/', views.movie_follow),
    path('<int:movie_pk>/reviews/', views.create_review),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_delete),
    path('<int:movie_pk>/reviews/<int:review_pk>/like/', views.like_review),
    path('<int:page_pk>/more/', views.more_movies),
]
