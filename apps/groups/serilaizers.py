# coding=utf-8
# auth: zhangyiling
# time: 2019-04-14 19:44
# description: 用户组序列化


from rest_framework import serializers
from django.contrib.auth.models import Group


class GroupSerializer(serializers.ModelSerializer):
    """
    用户组序列化类
    """

    class Meta:
        model = Group
        fields = ("id", "name")
