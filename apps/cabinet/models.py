from django.db import models
from idcs.models import IDC


class Cabinet(models.Model):
    """
    机柜
    """
    idc = models.ForeignKey(IDC, verbose_name='所在机房')
    name = models.CharField(max_length=255, null=False, verbose_name='机柜名称')

    class Meta:
        db_table = 'resources_cabint'  # 表名
        ordering = ['id']  # 排序

    def __str__(self):
        """
        打印模型现实的名字
        """
        return self.name
