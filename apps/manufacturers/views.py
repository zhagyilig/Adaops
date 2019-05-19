from rest_framework import viewsets
from .models import Manufacturers, ProductModel
from .serializers import ManufacturerSerializer, ProductModelSerializer


class ManufacturerViewset(viewsets.ModelViewSet):
    """
    retrieve:
        返回指定厂商信息
    list:
        返回厂商信息
    update:
        更新厂商信息
    detroy:
        删除厂商记录
    crate:
        创建厂商记录
    partial_update:
        更新厂商部分记录
    """
    queryset = Manufacturers.objects.all()
    serializer_class = ManufacturerSerializer


class ProductModelViewset(viewsets.ModelViewSet):
    """
    retrieve:
        返回指定厂品型号信息
    list:
        返回厂品型号信息
    update:
        更新厂品型号信息
    detroy:
        删除厂品型号记录
    crate:
        创建厂品型号记录
    partial_update:
        更新厂品型号部分记录
    """
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer