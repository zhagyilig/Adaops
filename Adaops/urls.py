# coding=utf-8
# auth: zhangyiling
# time: 2019/3/9 下午3:53
# description: Adaops URL Configuration


from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
# 接口文档, pip install coreapi
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token  # JWT

# viewset
from idcs.views import IdcViewset
from users.views import UserViewset
from cabinet.views import CabinetViewset
from manufacturers.views import ManufacturerViewset, ProductModelViewset
from servers.views import ServerAutoReportViewset, IPViewset, NetworkDeviceViewset, ServerViewset

# route
route = DefaultRouter()
route.register('idcs', IdcViewset, base_name='idcs')  # 机房
route.register('users', UserViewset, base_name='users')  # 用户管理
route.register('cabinet', CabinetViewset, base_name='cabinet')  # 机柜
route.register(
    'manufacturer',
    ManufacturerViewset,
    base_name='manufacturer')  # 厂商
route.register(
    'productModel',
    ProductModelViewset,
    base_name='productModel')  # 厂品型号
route.register('serverAutoReport', ServerAutoReportViewset,
               base_name='serverAutoReport')  # 服务器资产信息自动提交
route.register('ip', IPViewset, base_name='ip')
route.register(
    'networkDevice',
    NetworkDeviceViewset,
    base_name='networkDevice')
route.register('server', ServerViewset, base_name='server')  # 服务器信息

# urlpatterns
urlpatterns = [
    url(r'^', include(route.urls)),
    url(r'^api-auth', include('rest_framework.urls', namespace='api-auth'), ),
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', obtain_jwt_token),  # JWT
    url(r'^docs/', include_docs_urls(title='运维平台接口文档'))
]
