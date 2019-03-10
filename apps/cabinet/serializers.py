# coding=utf-8
# auth: zhangyiling
# time: 2019/3/10 下午3:09
# description: 机柜数据序列化

from rest_framework import serializers
from idcs.serializers import IdcSerializers
from idcs.models import IDC
from .models import Cabinet


class CabinetSerializer(serializers.Serializer):
    """
    序列化类
    """
    # 拿到 idc 全部数据
    # idc = IdcSerializers(many=False)

    # idc 是通过 pk 关联, 关联模式(一对一, 一对多, 多对多)是通过 many
    # IdcSerializers  => <class 'idcs.serializers.IdcSerializers'>
    # queryset = IDC.objects.all() => 关联的来源数据
    idc = serializers.PrimaryKeyRelatedField(many=False, queryset=IDC.objects.all())
    name = serializers.CharField(required=True)

    # 既要 id, 也需要 name
    # representation 表现, 陈述
    def to_representation(self, instance):
        """
        序列化转化成 json 的最后一步
        将上面的成员属性, 序列化成字典
        ex: OrderedDict([('idc', 1), ('name', 'test')])
        """
        # print(type(instance))  # 机柜的对象: <class 'cabinet.models.Cabinet'>
        # print(type(instance.idc))  # <class 'idcs.models.IDC'>
        # print(instance)  # 机柜 ex: test
        # print(instance.idc)  # 机房 ex: 香港机房

        idc_obj = instance.idc
        ret = super(CabinetSerializer, self).to_representation(instance)
        ret['idc'] = {
            'id': idc_obj.id,
            'name': idc_obj.name
        }
        # print(ret)  # OrderedDict([('idc', 1), ('name', 'test')])
        return ret

    def to_internal_value(self, data):
        """
        反序列化的第一步： 拿到提交过来的原始数据: QueryDict
        """
        # <QueryDict: {'csrfmiddlewaretoken': ['Qw1WHJgJJkkPj39pmn7mpVtV1lxwJnrusvf6dTSm8QMtE190nHUkdcbJWbAOlkre'], 'idc': ['11'], 'name': ['test5']}>
        # print(data) # 数据从 requst.body 中获取
        return super(CabinetSerializer, self).to_internal_value(data)

    def create(self, validated_data):
        # print(validated_data) # {'idc': <IDC: 湖北机房>, 'name': 'test3'}
        return Cabinet.objects.create(**validated_data)

