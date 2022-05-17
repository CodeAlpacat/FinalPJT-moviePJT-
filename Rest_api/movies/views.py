
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers.movie import MovieListSerializer, MovieSerializer
from .models import Movie

#날짜정보
import datetime
date = datetime.datetime.now()

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
    serializers = MovieListSerializer(movies, many=True)
    
    for movie in serializers.data:
        if movie['release_date'][0:4] == str(date.year):
            if int(movie['release_date'][5:7]) == date.month:
                #같은 달에 출시했다면, 현재 날짜가 2주 이상
                if int(movie['release_date'][8:]) <= date.day and 14<= date.day <= 29:
                    pass #리스트에 추가
            #현재 날짜가 14일 이전이라면, 이전 달까지 계산
            elif movie['release_date'][5:7] == (date.month - 1):
                
        
    

    return Response(serializers.data)