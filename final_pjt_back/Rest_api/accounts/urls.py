from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/<username>/', views.profile_or_edit),
    path('<int:user_pk>/follow/', views.follow),
]
