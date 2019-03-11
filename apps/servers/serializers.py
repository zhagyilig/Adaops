# coding=utf-8
# auth: zhangyiling
# time: 2019/3/11 下午11:19
# description: 服务器序列化器


from rest_framework import serializers
from servers.models import Server, NetworkDevice, IP


class ServerSerializer(serializers.ModelSerializer):
    """
    服务器序列化
    """

    class Meta:
        model = Server
        fields = '__all__'


class NetworkDeviceSerializer(serializers.ModelSerializer):
    """
    网卡序列化
    """

    class Meta:
        model = NetworkDevice
        fields = '__all__'


class IPSerializer(serializers.ModelSerializer):
    """
    IP地址序列化
    """

    class meta:
        model = IP
        fiedls = '__all__'
