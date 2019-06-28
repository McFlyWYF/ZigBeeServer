from rest_framework import serializers
from .models import User, Foods, Message


class FoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(read_only=True, )

    class Meta:
        model = Message
        fields = ('account', 'messageId', 'heartData', 'degreeData', 'time', 'alarm')


class UserSerializer(serializers.ModelSerializer):
    message = MessageSerializer(source='message_set', read_only=True, many=True, )  # 一对多关系

    class Meta:
        model = User
        fields = ('account', 'sex', 'age', 'message')
