from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from .serializers import ProfileSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET', 'PUT'])
def profile_or_edit(request, username):

    user = get_object_or_404(get_user_model(), username=username)
    if request.method == 'GET':
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
    
    elif request.user.is_authenticated:
        serializer = ProfileSerializer(data=request.data, instance=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        



@api_view(['POST'])
def follow(request, user_pk):
    you = get_object_or_404(get_user_model(), pk=user_pk)
    me = request.user

    if you.followers.filter(pk=me.pk).exists():
    # if me in you.followers.all():
        # 언팔로우
        you.followers.remove(me)
        serializer = ProfileSerializer(you)
        return Response(serializer.data)
    else:
        # 팔로우
        you.followers.add(me)
        serializer = ProfileSerializer(you)
        return Response(serializer.data)
