from django.urls import path
from . import views
app_name = 'community'

urlpatterns = [
    path('', views.article_list_or_create),
    path('<int:article_pk>/', views.article_detail_or_update_or_delete),
    path('<int:article_pk>/like/', views.like_article),
    path('<int:article_pk>/comments/', views.create_comment),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),
    #댓글에 달린 좋아요의 갯수를 통해 베스트 댓글 순으로 정렬
    path('<int:article_pk>/comments/<int:comment_pk>/like/', views.like_comment),
]
