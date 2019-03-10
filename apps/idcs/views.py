import logging
from rest_framework import viewsets
from .models import IDC
from .serializers import IdcSerializers

logger = logging.getLogger(__name__)


class IdcViewset(viewsets.ModelViewSet):
    """
    retrieve:
        返回指定IDC信息
    list:
        返回IDC信息
    update:
        更新IDC信息
    detroy:
        删除IDC记录
    crate:
        创建IDC记录
    partial_update:
        更新部分记录
    """
    queryset = IDC.objects.all()
    serializer_class = IdcSerializers
