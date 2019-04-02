# coding=utf-8
# auth: zhangyiling
# time: 2019-03-21 07:10
# description:


import logging
import django_filters
from .models import Server
from django.db.models import Q


class ServerFilter(django_filters.FilterSet):
    """
    服务器信息查询搜索类
    """
    # 提供搜索的方式及字段
    hostname = django_filters.CharFilter(lookup_expr='icontains')

    # 提供搜索的modle和字段
    class Meta:
        model = Server
        fields = ['hostname', 'ip', 'os', ]


class ServersFiter(django_filters.FilterSet):
    """
    服务器信息查询搜索类
    """
    # 提供搜索的方式及字段
    hostname = django_filters.CharFilter(method='search_server')

    def search_server(self, queryset, name, value):
        """
        主机名/ip搜索
        """
        return queryset.filter(Q(hostname__icontains=value) | Q(ip__icontains=value))
