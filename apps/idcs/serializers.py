# coding=utf-8
# auth: zhangyiling
# time: 2019/3/9 下午4:12
# description: 序列化云厂商数据

import logging
# 序列化器, 把数据包装成类似字典格式
from rest_framework import serializers
from .models import IDC

logger = logging.getLogger(__name__)


class IdcSerializers(serializers.Serializer):
    """云厂商序列化."""
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=32, label='机房名称',help_text='机房名称',
                                 error_messages={'blank': '字段不能为空', 'required': '必要字段'})
    address = serializers.CharField(required=True, max_length=200, label='机房地址',help_text='机房地址')
    phone = serializers.CharField(required=True, max_length=20, label='联系电话', help_text='联系电话')
    email = serializers.EmailField(required=True, label='邮件',help_text='邮件')
    letter = serializers.CharField(required=True, max_length=8, label='简称', help_text='简称')

    # validated_data 是验证之后的数据(有序字典)
    def create(self, validated_data):
        """添加数据."""
        print('validated_data: {}'.format(validated_data))
        return IDC.objects.create(**validated_data)

    # instance 当前的对象(IdcSerializers)
    def update(self, instance, validated_data):
        """更新指定字段."""
        print('instance: %s' % instance)
        print('validated_data: %s' % validated_data)
        # 可以允许更新的字段
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
