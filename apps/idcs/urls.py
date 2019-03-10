# coding=utf-8
# auth: zhangyiling
# time: 2019/3/9 下午3:53
# description: idcs URL Configuration


from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

## 版本一
urlpatterns = [
    url(r'^idcs/$', views.idc_list),
    url(r'^idcs/(?P<pk>[0-9]+)', views.idc_detail),
]

# 版本二
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^idcs/$', views.idc_list_v2, name='idc_list'),
    url('^idc_detail_v2/(?P<pk>[0-9]+)/$', views.idc_detail_v2, name='idc_detail'),
    url(r'^idc_list/$', views.VIdcList.as_view(), name='idc_Vlist'),
    url(r'^idc_detail_v3/(?P<pk>[0-9]+)/$', views.VIdcDetail.as_view(), name='idc_Vdetail'),
]

# 版本四
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^idcs/$', views.IdcList_v4.as_view(), name='idc_list'),
    url('^idc_detail_v2/(?P<pk>[0-9]+)/$', views.idc_detail_v2, name='idc_detail'),
    url(r'^idc_list/$', views.VIdcList.as_view(), name='idc_Vlist'),
    url(r'^idc_detail_v3/(?P<pk>[0-9]+)/$', views.VIdcDetail.as_view(), name='idc_Vdetail'),
    url(r'^idc_detail_v4/(?P<pk>[0-9]+)/$', views.IdcDetail_v4.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# 版本五
idc_list = views.IdcListViewset.as_view({
    'get': 'list',
    'post': 'create'
})

idc_detail = views.IdcListViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^idcs/$', idc_list, name='idc_list'),
    url(r'^idc_detail_v5/(?P<pk>[0-9]+)/$', idc_detail),
]

# 版本六
from rest_framework.routers import DefaultRouter

route = DefaultRouter()

route.register('idcs', views.IdcViewset_v6)
urlpatterns = [
    url(r'^', include(route.urls))
]
