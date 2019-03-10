# coding=utf-8
# auth: zhangyiling
# time: 2019/3/10 下午7:33
# description:


from rest_framework import serializers
from .models import ProductModel, Manufacturers


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
