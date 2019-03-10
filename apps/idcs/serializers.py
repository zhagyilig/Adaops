# coding=utf-8
# auth: zhangyiling
# time: 2019/3/9 下午4:12
# description: 序列化IDC数据


from rest_framework import serializers  # 序列化器，把数据包装成类似字典的格式
from .models import IDC


class IdcSerializers(serializers.Serializer):
    """
    Idc 序列化类，自动生成接口文档
    序列化：1. 模型 2. 序列化 3. 视图
    """
    id = serializers.IntegerField(read_only=True)  # 数据类型也是前端访问的类型
    name = serializers.CharField(required=True, max_length=32, label='机房名称',
                                 help_text='机房名称',
                                 error_messages={'blank': '字段不能为空',
                                                 'required': '必要字段'})
    address = serializers.CharField(required=True, max_length=200, label='机房地址')
    phone = serializers.CharField(required=True, max_length=20, label='联系电话')
    email = serializers.EmailField(required=True, label='邮件')
    letter = serializers.CharField(required=True, max_length=8, label='简称')

    # validated_data 验证之后的数据
    def create(self, validated_data):
        return IDC.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print('+++instance: %s' % instance)
        print('+++validated_data: %s' % validated_data)
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
