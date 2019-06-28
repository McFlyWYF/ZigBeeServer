from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.

from .serializers import UserSerializer, MessageSerializer, FoodsSerializer
from .models import User, Foods, Message
from django.views.decorators.csrf import csrf_exempt
from myapp import models
from django.http.response import HttpResponse
import json


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


# 传送数据
@csrf_exempt
def data(request):
    heart = request.GET.get("heart")
    degree = request.GET.get("degree")
    time = request.GET.get("time")
    alarm = request.GET.get("alarm")
    account = request.GET.get("account")

    if request.method == 'POST':
        # heart = request.POST.get('heart')  # 用户名
        # degree = request.POST.get('degree')  # 密码
        # time = request.POST.get('time')  # 年龄
        # alarm = request.POST.get('alarm')
        # account = request.POST.get('account')

        print(heart, degree, time, alarm, account)
        message = models.Message.objects.create(heartData=heart, degreeData=degree, time=time, alarm=alarm,
                                                account=User.objects.get(account=account))
        message.save()
        resp = {'message': "上传成功"}
        return HttpResponse(json.dump(resp))
    else:
        resp = {'message': "上传失败"}
        return HttpResponse(json.dump(resp))


# 注册
@csrf_exempt
def register(request):
    if request.method == 'POST':
        account = request.POST.get('account')  # 用户名
        password = request.POST.get('password')  # 密码
        age = request.POST.get('age')  # 年龄
        sex = request.POST.get('sex')

        # print(account, password, age, sex)
        user = models.User.objects.create(account=account, password=password, age=age, sex=sex)
        user.save()
        resp = {'message': "注册成功"}
        return HttpResponse(json.dumps(resp))
    else:
        resp = {'message': "该用户已存在"}
        return HttpResponse(json.dumps(resp))


# 登录
@csrf_exempt
def login(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')
        user = User.objects.filter(account=account, password=password)
        if user:
            resp = {'message': "登录成功"}
            return HttpResponse(json.dumps(resp))
        else:
            resp = {'message': "登录失败"}
            return HttpResponse(json.dumps(resp))
