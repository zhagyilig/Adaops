# coding=utf-8
# auth: zhangyiling
# time: 2019/3/10 上午1:33
# description: 厂商和型号序列化


import logging
from rest_framework import serializers
from .models import ProductModel, Manufacturers

logger = logging.getLogger(__name__)


class ManufacturerSerializer(serializers.ModelSerializer):
    """
    厂商序列化类, 使用序列化类
    """

    class Meta:
        model = Manufacturers
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    """
    厂品型号序列化类, 使用序列化类
    """

    class Meta:
        model = ProductModel
        fields = '__all__'

    # 验证的顺序: 序列化->自定义->对象级别
    def validata_model_name(self, value):
        """
        字段级别验证, Usage: validata_+字段名
        """
        print('value: {}'.format(value))
        # 转换成对象
        return value

    def validate(self, attrs):
        """
        对象级别验证
        """
        # OrderedDict([('model_name', 'yyyy'), ('vendor', <Manufacturers: DELL>)])
        # print('attrs: {}'.format(attrs))
        manufacturer_obj = attrs['vendor']  # DELL
        try:
            # 反向查询
            manufacturer_obj.productmodel_set.get(model_name__exact=attrs['model_name'])
            raise serializers.ValidationError('该型号已经存在!')
        except ProductModel.DoesNotExist:
            return attrs

    def to_representation(self, instance):
        """
        序列化转化成 json 的最后一步
        将上面的成员属性, 序列化成字典
        ex: OrderedDict([('idc', 1), ('name', 'test')])
        """
        manufacturer_obj = instance.vendor  # ex: DELL
        # OrderedDict([('id', 2), ('model_name', 'xxxxx'), ('vendor', {'id': 1, 'name': 'DELL'})])
        ret = super(ProductModelSerializer, self).to_representation(instance)
        ret['vendor'] = {
            'id': manufacturer_obj.id,
            'name': manufacturer_obj.vendor_name
        }
        return ret

