from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from .serializers import UserSerializer, MessageSerializer, FoodsSerializer
from .models import User, Foods, Message


class UserSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FoodsSet(viewsets.ModelViewSet):
    queryset = Foods.objects.all()
    serializer_class = FoodsSerializer


class MessageSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = 'account'
