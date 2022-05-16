from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers.movie import MovieListSerializer, MovieSerializer
from .models import Movie

# import requests, json



# Create your views here.

@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializers = MovieListSerializer(movies, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    serializers = MovieSerializer(movie)
    return Response(serializers.data)

# def get_movie_genre(request):
#     genre_url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=c0ea5b6535679915d16aada2f7427157&language=en-US'
#     genre_data = json.load(genre_url.text)
#     print(genre_data)