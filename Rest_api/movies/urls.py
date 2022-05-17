from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('upcoming/',views.upcoming_movie_list),
    path('nowplaying/', views.nowplaying_movie_list),
]