
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers.movie import MovieListSerializer, MovieSerializer
from .models import Movie

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
    
    return Response(serializers.data)


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

    return Response(now_playing_list)