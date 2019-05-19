# coding=utf-8
# auth: zhangyiling
# time: 2019-04-14 19:50
# description: 用户组信息搜索

import django_filters
from django.contrib.auth.models import Group

class GroupFilter(django_filters.FilterSet):
    """
    用户组搜索类
    """

    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Group
        fields = ['name']