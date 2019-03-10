from rest_framework import viewsets
from .models import Cabinet
from .serializers import CabinetSerializer


class CabinetViewset(viewsets.ModelViewSet):
    """
    retrieve:
        返回指定机房信息
    list:
        返回机房信息
    update:
        更新机房信息
    detroy:
        删除机房记录
    crate:
        创建机房记录
    partial_update:
        更新部分记录
    """
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer
