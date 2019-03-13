# coding=utf-8
# auth: zhangyiling
# time: 2019/3/11 下午11:19
# description: 服务器序列化器

import logging
from rest_framework import serializers
from manufacturers.models import Manufacturers, ProductModel
from servers.models import Server, NetworkDevice, IP

logger = logging.getLogger(__name__)


class ServerAutoReportSerializer(serializers.Serializer):
    """
    服务器序列化, 使用Serializer
    序列化使用到多张表，使用ModelSerializer不合适
    """
    ip = serializers.IPAddressField(required=True, help_text='ip地址')
    hostname = serializers.CharField(required=True, max_length=50)
    cpu = serializers.CharField(required=True)
    mem = serializers.CharField(required=True)
    disk = serializers.CharField(required=True)  # 可以做成一对多
    os = serializers.CharField(required=True)
    # 不能使用下面的方式，# 前端传入的是厂商的名称是str，需要验证
    # manufacturer = serializers.PrimaryKeyRelatedField(many=False, queryset=Manufacturers.objects.all())
    manufacturer = serializers.CharField(required=True)  # 前端传入的是厂商的名称，需要验证
    model_name = serializers.CharField(required=True)
    uuid = serializers.CharField(required=True)

    def validate_manufacturer(self, value):
        """
        value: 前端传过来的manufacturer
        验证制造商: 转换成制造商的对象
        """
        print('1 +++value: %s' % value)
        try:
            manufacturers = Manufacturers.objects.get(vendor_name__exact=value)
            print('+++ 2 manufacturers: %s' % manufacturers)
            return manufacturers
        except Manufacturers.DoesNotExist:
            return self.create_manufacturers(value)

    def create_manufacturers(self, vendor_name):
        """
        创建制造商: 返回一个对象
        """
        print('+++6')
        return Manufacturers.objects.create(vendor_name=vendor_name)

    def validate(self, attrs):
        print('3 +++atters: %s' % attrs)  # OrdereDict
        manufacturer_obj = attrs['manufacturer']  # <Manufacturers: ali>
        try:
            attrs['model_name'] = manufacturer_obj.productmodel_set.get(model_name__exact=attrs['model_name'])
        except ProductModel.DoesNotExist:
            attrs['model_name'] = self.create_product_model(manufacturer_obj, attrs['model_name'])
        return attrs

    def create_product_model(self, manufacturer_obj, model_name):
        """
        创建产品型号
        """
        print('5 +++%s %s' % (manufacturer_obj, model_name))
        return ProductModel.objects.create(model_name=model_name, vendor=manufacturer_obj)

    def create(self, validated_data):
        """
        将数据写入Servers表中
        {'ip': '192.168.199.188',
         'hostname': 'django-node-1',
         'cpu': '8',
         'mem': '32',
         'disk': '32',
         'os': 'Debian9.6',
         'manufacturer': <Manufacturers: ali>,
         'model_name': <ProductModel: ec2>,
         'uuid': '88888888'}
         """
        print('6 +++validated_data: %s' % validated_data)
        return Server.objects.create(**validated_data)


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
