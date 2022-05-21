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
    path('<int:movie_pk>/movie_follow/', views.movie_follow),
]
