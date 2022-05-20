import json
from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Count

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article, Comment
from .serializers.articles import ArticleListSerializer, ArticleSerializer
from .serializers.comments import CommentSerializer

##게시글 리스트 조회 및 개별 게시글 작성
@api_view(['GET', 'POST'])
def article_list_or_create(request):
    
    def article_list():
        articles = Article.objects.annotate(
            comment_count = Count('comments', distinct=True),
            like_count = Count('liked_users', distinct=True)
        ).order_by('-pk')
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    def create_article():
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return article_list()
    elif request.method == 'POST':
        return create_article()

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_or_update_or_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    def article_detail():
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def update_article():
        if request.user == article.user:
            serializer = ArticleSerializer(instance=article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    def delete_article():
        if request.user == article.user:
            article.delete()
            data= {
                'delete':'삭제가 완료되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return article_detail()
    elif request.method == 'PUT':
        if request.user == article.user:
            return update_article()
    elif request.method == 'DELETE':
        if request.user == article.user:
            return delete_article()

#유저가 게시글에 좋아요
#이미 눌렀다면 유저 정보 삭제 / 없다면 좋아요
@api_view(['POST'])
def like_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    if article.liked_users.filter(pk=user.pk).exists():
        article.liked_users.remove(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    else:
        article.liked_users.add(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

#댓글 생성
@api_view(['POST'])
def create_comment(request, article_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)
    
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=user) #현재 유저와 게시글 정보 저장
        comments = article.comments.all()#댓글을 입력하는 도중에 댓글 업데이트
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def update_comment():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                comments = article.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)
    
    def delete_comment():
        if request.user == comment.user:
            comment.delete()
            comments = article.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()
    
    

@api_view(['POST'])
def like_comment(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    #댓글이 달린 게시글 필드 정보와 게시글의 pk가 같아야 좋아요 가능
    user = request.user
    serializer = CommentSerializer(comment)
    if article.pk == serializer.data.get('article'):
        if comment.liked_users.filter(pk=user.pk).exists():
            comment.liked_users.remove(user)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        else:
            comment.liked_users.add(user)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
    #만약 댓글과 게시글이 다른 경우에는 203 에러 출력
    else:
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)