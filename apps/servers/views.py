from rest_framework import viewsets, mixins
from servers.models import Server, NetworkDevice, IP
from .serializers import ServerAutoReportSerializer, NetworkDeviceSerializer, IPSerializer


class ServerAutoReportViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    list:
        获取服务器列表
    create:
        创建服务器
    """
    queryset = Server.objects.all()
    serializer_class = ServerAutoReportSerializer


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
