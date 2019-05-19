import logging
from rest_framework import viewsets
from .models import IDC
from .serializers import IdcSerializers

logger = logging.getLogger(__name__)


class IdcViewset(viewsets.ModelViewSet):
    """
    retrieve:
        返回指定云厂商信息
    list:
        返回云厂商信息
    update:
        更新云厂商信息
    detroy:
        删除云厂商记录
    crate:
        创建云厂商记录
    partial_update:
        更新云厂商部分记录
    """
    queryset = IDC.objects.all()
    serializer_class = IdcSerializers
