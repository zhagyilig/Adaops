import logging
from rest_framework import viewsets
# from django.contrib.auth.models import User  # 后期使用下一行方式
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()  # 实例化用户模型
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
