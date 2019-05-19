# coding=utf-8
# auth: zhangyiling
# time: 2019-04-14 19:53
# description: 用户组路由配置

from rest_framework.routers import DefaultRouter
from groups.views import GroupsViewset

group_router = DefaultRouter()
group_router.register('Groups', GroupsViewset, base_name='Groups')
