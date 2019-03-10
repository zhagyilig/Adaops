from django.db import models

class Manufacturers(models.Model):
    """
    厂商/云平台
    """
    vendor_name = models.CharField(max_length=32, db_index=True,unique=True,verbose_name='厂商名称',help_text='厂商名称')
    tel = models.CharField(max_length=15, null=True, verbose_name='联系电话', help_text='联系电话')
    mail = models.CharField(max_length=32, null=True, verbose_name='联系邮件',help_text='厂商名称')
    remark = models.CharField(max_length=255, null=True, verbose_name='备注',help_text='备注')

    def __str__(self):
        return self.vendor_name

    class Meta:
        db_table = 'resources_manufacturers'
        ordering = ['id']


class ProductModel(models.Model):
    """
    厂品型号
    """
    model_name = models.CharField(max_length=20, verbose_name='型号名称',help_text='型号名称')
    vendor = models.ForeignKey(Manufacturers, verbose_name='所属制造商',help_text='所属制造商')

    def __str__(self):
        return self.model_name

    class Meta:
        db_table = 'resources_productmodel'
        ordering = ['id']


