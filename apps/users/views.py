import logging
from rest_framework import viewsets
# from django.contrib.auth.models import User  # 后期使用下一行方式
from django.contrib.auth import get_user_model
# from django_filters.rest_framework import DjangoFilterBackend  # 全局已经配置
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .userFilter import UserFilter

# 实例化用户模型
User = get_user_model()

logger = logging.getLogger(__name__)


class UserViewset(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        返回用户信息
    list:
        返回用户列表
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    ## 搜索
    filter_class = UserFilter
    # 全局已经配置
    # filter_backends = (DjangoFilterBackend, )
    # filter_fields = ('username', )

    ## 认证
    # 使用了全局配置, 所以注释下面代码
    # 不使用全局配置, 自定义权限配置
    # authentication_classes = (SessionAuthentication, )
    # permission_classes = (IsAuthenticated, )
