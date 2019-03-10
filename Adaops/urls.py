# coding=utf-8
# auth: zhangyiling
# time: 2019/3/9 下午3:53
# description: Adaops URL Configuration


from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls  # 接口文档, pip install coreapi

# views
from idcs.views import IdcViewset
from users.views import UserViewset
from cabinet.views import CabinetViewset
from manufacturers.views import ManufacturerViewset
from manufacturers.views import ProductModelViewset

# route
route = DefaultRouter()
route.register('idcs', IdcViewset, base_name='idcs')  # 机房
route.register('users', UserViewset, base_name='users')  # 用户管理
route.register('cabinet', CabinetViewset, base_name='cabinet')  # 机柜
route.register('manufacturer', ManufacturerViewset, base_name='manufacturer')  # 厂商
route.register('productModel', ProductModelViewset, base_name='productModel') # 厂品型号

# urlpatterns
urlpatterns = [
    url(r'^', include(route.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='运维平台接口文档'))
]
