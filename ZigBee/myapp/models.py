from django.db import models

# Create your models here.


'''
用户表
'''


class User(models.Model):
    account = models.CharField(max_length=50, primary_key=True)  # 用户名
    password = models.CharField(max_length=50, null=False)  # 密码
    sex = models.CharField(max_length=10)  # 性别
    age = models.IntegerField()  # 年龄

    def __str__(self):
        return self.account


'''
食物表
'''


class Foods(models.Model):
    foodId = models.IntegerField(primary_key=True, auto_created=True)  # 编号
    foodName = models.CharField(max_length=100, null=False)  # 名字
    foodUrl = models.URLField(max_length=100)  # 食物URL
    foodmaterial = models.CharField(max_length=100)  # 食材
    foodVariety = models.CharField(max_length=20)  # 食物种类

    def __str__(self):
        return self.foodName


'''
数据表
'''


class Message(models.Model):
    messageId = models.IntegerField(primary_key=True, auto_created=True)  # id
    heartData = models.FloatField(max_length=50)  # 心率
    degreeData = models.FloatField(max_length=50)  # 体温
    time = models.CharField(max_length=50)  # 时间
    alarm = models.IntegerField()  # 报警标志
    account = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.time
