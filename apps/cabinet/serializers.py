# coding=utf-8
# auth: zhangyiling
# time: 2019/3/10 下午3:09
# description: 机柜数据序列化

import logging
from rest_framework import serializers
from idcs.serializers import IdcSerializers
from idcs.models import IDC
from .models import Cabinet

logger = logging.getLogger(__name__)


class CabinetSerializer(serializers.Serializer):
    """机柜信息序列化类."""
    # idc 全部数据
    # idc = IdcSerializers(many=False)

    # idc 是通过 pk 关联, 关联(一对一, 一对多, 多对多)是通过 many 参数; 一对多, 多对多:many=True
    # 关联数据 queryset = IDC.objects.all()
    # 关联关系都可以使用 PrimaryKeyRelatedField
    idc = serializers.PrimaryKeyRelatedField(queryset=IDC.objects.all(), many=False)
    name = serializers.CharField(required=True)

    def to_representation(self, instance):
        """
        前端不仅需要显示 id 字段, 也需要显示 name 字段;
        将上面属性字段, 序列化成 dict: ex: OrderedDict([('idc', 1), ('name', 'test')])
        """
        # print(type(instance))  # 机柜对象: <class 'cabinet.models.Cabinet'>
        # print(type(instance.idc))  # idc对象: <class 'idcs.models.IDC'>
        # print(instance)  # 机柜: test
        # print(instance.idc)  # 机房: 香港机房

        idc_obj = instance.idc
        ret = super(CabinetSerializer, self).to_representation(instance)
        ret['idc'] = {
            'id': idc_obj.id,
            'name': idc_obj.name
        }
        # print(ret)
        # OrderedDict([('idc', 1), ('name', 'test')])
        return ret

    def to_internal_value(self, data):
        """反序列化的第一步, 获取提交的原始数据: QueryDict => request.GET / request.POST."""
        print(data)  # 数据从 requst.body 中获取
        # <QueryDict: {'csrfmiddlewaretoken': ['xxx'], 'idc': ['11'], 'name': ['test5']}>
        return super(CabinetSerializer, self).to_internal_value(data)

    def create(self, validated_data):
        """添加数据."""
        print(validated_data)
        # {'idc': <IDC: 湖北机房>, 'name': 'test3'}
        return Cabinet.objects.create(**validated_data)
