from custom_pagination import Pagination
from rest_framework import viewsets, mixins
from servers.models import Server, NetworkDevice, IP
from .serializers import ServerAutoReportSerializer, NetworkDeviceSerializer, \
    IPSerializer, ServerSerializer
from .serversFilter import ServerFilter, ServersFiter


class ServerAutoReportViewset(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """
    create:
        自动导入服务器信息
    """
    queryset = Server.objects.all()
    serializer_class = ServerAutoReportSerializer


class ServerViewset(viewsets.ReadOnlyModelViewSet):
    """
    list:
        获取服务器信息
    retrieve:
        获取一台服务器信息
    """
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    filter_class = ServersFiter
    pagination_class = Pagination

class NetworkDeviceViewset(viewsets.ReadOnlyModelViewSet):
    """
    list:
        显示网络设备
    retrieve:
        显示指定的一条网络设备信息
    """
    queryset = NetworkDevice.objects.all()
    serializer_class = NetworkDeviceSerializer


class IPViewset(viewsets.ReadOnlyModelViewSet):
    """
    list:
        显示ip地址
    retrieve:
        显示指定的一条ip信息
    """
    queryset = IP.objects.all()
    serializer_class = IPSerializer
