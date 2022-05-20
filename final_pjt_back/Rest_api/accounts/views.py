from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from .serializers import ProfileSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)