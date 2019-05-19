# coding=utf-8
# auth: zhangyiling
# time: 2019-03-21 00:03
# description: 用户查询搜索


import logging
import django_filters
from django.contrib.auth import get_user_model

User = get_user_model()
logger = logging.getLogger(__name__)


class UserFilter(django_filters.FilterSet):
    """用户查询搜索类."""
    # 提供搜索的方式
    username = django_filters.CharFilter(lookup_expr='iexact', label='用户名')  # 不区分大小写
    logging.info('搜索User: {}'.format(username))

    # 提供搜索的 modle 和字段
    class Meta:
        model = User
        fields = ['username', ]
