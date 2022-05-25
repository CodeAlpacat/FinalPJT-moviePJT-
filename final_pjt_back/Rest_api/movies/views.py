
from django.shortcuts import render
from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers.movie import MovieListSerializer, MovieSerializer
from .serializers.genre import GenreListSerializer
from .serializers.review import ReviewSerializer
from .models import Genre, Movie, Review
from django.contrib.auth import get_user_model

from random import randint
import json

#날짜정보
from datetime import datetime
from dateutil.relativedelta import relativedelta
date = datetime.now()

#전체 영화 가져오기
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializers = MovieListSerializer(movies, many=True)
    return Response(serializers.data)

#특정 id의 영화 가져오기
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    movie.reviews = movie.reviews.order_by('-pk')
    movie.save()
    serializers = MovieSerializer(movie)
    return Response(serializers.data)

#2022년 5월 20일 이후 출시하는 영화 정보 가져오기
@api_view(['GET'])
def upcoming_movie_list(request):
    movies = get_list_or_404(Movie)
    serializers = MovieListSerializer(movies, many=True)
    upcoming_movies = []
    for movie in serializers.data:
        if movie['release_date'][0:7] == '2022-06' or movie['release_date'][0:9] == '2022-05-2' :
            upcoming_movies.append(movie)
    
    if len(upcoming_movies) > 10:
        return Response(upcoming_movies[:10])
    return Response(upcoming_movies)


#출시한지 2주 내의 영화를 가져오기
@api_view(['GET'])
def nowplaying_movie_list(request):
    movies = get_list_or_404(Movie)
    serializers_1 = MovieListSerializer(movies, many=True)
    
    now_playing_list = []
    # release_date 예시: 2022-05-17
    for movie in serializers_1.data:
        if movie['release_date'][0:4] == str(date.year):
            if int(movie['release_date'][5:7]) == date.month:
                #같은 달에 출시했다면, 현재 날짜가 2주 이상
                if  0 < date.day - int(movie['release_date'][8:]) <= 14:
                    #리스트에 추가
                    now_playing_list.append(movie)
            #현재 날짜가 14일 이전이라면, 이전 달까지 계산 ( 1달 차이 )
            elif int(movie['release_date'][5:7]) == ((date - relativedelta(month=1)).month):
                # 현재 날짜기준 2주 전이 개봉일 이전인지 확인
                if (date - relativedelta(weeks=2)).month == int(movie['release_date'][5:7]):
                    if 0 < int(movie['release_date'][8:]) - (date - relativedelta(weeks=2)).day <= 14:
                        #리스트에 추가
                        now_playing_list.append(movie)   
    # serializers_2 = MovieListSerializer(now_playing_list, many=True)

    if len(now_playing_list) > 10:
        return Response(now_playing_list[:10])
    return Response(now_playing_list)



@api_view(['GET'])
def recommend_movie_list(request, user_pk):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    user = get_object_or_404(get_user_model(), pk=user_pk) # 현재 접속한 유저
    recommend_list = [] # 추천 리스트
    recommend_check = [] # 중복 확인 리스트
    lottery_list = [] # 로또 리스트
    number_list = [] # 추첨번호 리스트
    
    user_likes_genre = json.loads(user.genre_likes).get("genre_likes") or []  # 유저가 좋아하는 장르 id 값
    total_range = 0 # range 변수

    for movie in serializer.data:
        genres = movie['genres'] # 영화가 보유한 장르 리스트

        count = 1 # 확률 가중치

        for genre in genres: # 영화 보유 장르에 대해
            if str(genre) in user_likes_genre: # 유저가 좋아하는 장르 id 값이 일치할때마다 4배 적용
                count = count << 4 # 0개 일치: 1 1개 일치: 16 2개 일치: 256 3개 일치: 4096
        lottery_list.append((total_range, total_range + count - 1, movie)) # total range 값, movie 튜플로 append
        total_range += count # total_range값 증가
    
    for _ in range(20): # 숫자 추첨 20번
        number_list.append(randint(0, total_range - 1))
    
    lot_len = len(lottery_list) # 추첨 항목 크기
    
    
    for number in number_list: # 추첨 번호 소속 범위 탐색
        middle = (lot_len - 1) // 2 # 이진 탐색 middle 값
        left = 0 # 좌
        right = lot_len - 1 # 우
        while True: 
            if lottery_list[middle][0] > number: # 최소값보다 작으면, right, middle값 갱신
                right = middle - 1
                middle = (right + left) // 2
                continue
            elif lottery_list[middle][1] < number: # 최대값보다 크면, left, middle값 갱신
                left = middle + 1
                middle = (right + left) // 2
                continue
            else: # 범위 만족시 while문 탈출
                break
        # 중복 체크
        if not lottery_list[middle][2]['id'] in recommend_check:
            recommend_list.append(lottery_list[middle][2]) # 찾은 movie append
            recommend_check.append(lottery_list[middle][2]['id'])

    if len(recommend_list) > 10:
        return Response(recommend_list[:10])
    return Response(recommend_list)

@api_view(['GET'])
def genres_list(request):
    genres = get_list_or_404(Genre)
    serializers = GenreListSerializer(genres, many=True)
    return Response(serializers.data)

#좋아하는 영화 내 프로필의 my movie list에 담기
@api_view(['POST'])
def movie_follow(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.kept_by_user.filter(pk=user.pk).exists():
        movie.kept_by_user.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.kept_by_user.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


# 리뷰 생성

@api_view(['POST'])
def create_review(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user, movie=movie) # 현재 유저와 영화 정보 저장
        reviews = movie.reviews.all().order_by('pk')
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 리뷰 제거

@api_view(['DELETE'])
def review_delete(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        review.delete()
        reviews = movie.reviews.all().order_by('pk')
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def like_review(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user
    serializer = ReviewSerializer(review)
    if movie.pk == serializer.data.get('movie'):
        if review.liked_users.filter(pk=user.pk).exists():
            review.liked_users.remove(user)
            reviews = movie.reviews.all().order_by('pk')
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
        else:
            review.liked_users.add(user)
            review.save()
            reviews = movie.reviews.all().order_by('pk')
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
    else:
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

@api_view(['GET'])
def more_movies(request, page_pk):
    movies = get_list_or_404(Movie)
    page_pk *= 10
    movies = movies[page_pk, page_pk+10]

    serializers = MovieListSerializer(movies, many=True)
    return Response(serializers.data)