# coding=utf-8
# auth: zhangyiling
# time: 2019/3/10 上午9:27
# description:

from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    """
    用户资源序列化类
    """
    username = serializers.CharField(required=True, max_length=150)  # 返回给前端调用的数据类型
    email = serializers.EmailField(required=True, max_length=254)
