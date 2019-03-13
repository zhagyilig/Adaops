# coding=utf-8
# auth: zhangyiling
# time: 2019/3/11 下午11:19
# description: 服务器序列化器


from rest_framework import serializers
from servers.models import Server, NetworkDevice, IP


class ServerAutoReportSerializer(serializers.Serializer):
    """
    服务器序列化, 使用Serializer
    序列化使用到多张表，使用ModelSerializer不合适
    """
    ip = serializers.IPAddressField(required=True,help_text='ip地址')
    hostname = serializers.CharField(required=True)
    cpu = serializers.CharField(required=True)
    mem = serializers.CharField(required=True)
    disk = serializers.CharField(required=True)
    os = serializers.CharField(required=True)
    manufacturer = serializers.CharField(required=True) # 前端传入的是厂商的名称，需要验证
    model_name = serializers.CharField(required=True)  # 前端传入的是厂商的名称，需要验证
    uuid = serializers.CharField(required=True)

    def validate_manufacturer(self, data):
        pass



    def create(self, validated_data):
        pass


'''
{
"ip": "192.168.199.188",
"hostname": "django-node-1",
"cpu": "8",
"mem": "32",
"disk": "32",
"os": "Debian9.6",
"manufacturer": "ali",
"model_name": "ecs",
"uuid": "88888888"
}
'''


class NetworkDeviceSerializer(serializers.ModelSerializer):
    """
    网卡序列化
    """

    class Meta:
        model = NetworkDevice
        # 序列化全部字段
        fields = '__all__'


class IPSerializer(serializers.ModelSerializer):
    """
    IP地址序列化
    """

    class meta:
        model = IP
        fiedls = '__all__'
