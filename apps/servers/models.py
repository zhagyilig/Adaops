from django.db import models
from idcs.models import IDC
from cabinet.models import Cabinet
from manufacturers.models import Manufacturers, ProductModel


class Server(models.Model):
    """
    服务器
    """
    ip = models.CharField("管理IP", max_length=32, default=None, db_index=True, help_text="管理IP")
    hostname = models.CharField("主机名", max_length=50, default=None, db_index=True, help_text="主机名")
    cpu = models.CharField("CPU信息", max_length=250, default=None, help_text="CPU信息")
    mem = models.CharField("内存信息", max_length=100, default=None, help_text="内存信息")
    disk = models.CharField("硬盘信息", max_length=300, null=True, help_text="硬盘信息")
    os = models.CharField("操作系统", max_length=100, default=None, help_text="操作系统")
    sn = models.CharField("SN", max_length=40, db_index=True, null=True, help_text="SN")
    manufacturer = models.ForeignKey(Manufacturers, verbose_name="制造商", null=True, help_text="制造商")
    model_name = models.ForeignKey(ProductModel, verbose_name="服务器型号", default=None, help_text="服务器型号")
    rmt_card_ip = models.CharField("远程管理卡IP", max_length=15, null=True, help_text="远程管理卡IP")
    idc = models.ForeignKey(IDC, verbose_name="所在机房", null=True, help_text="所在机房")
    cabinet = models.ForeignKey(Cabinet, verbose_name="所在机柜", null=True, help_text="所在机柜")
    cabinet_position = models.CharField("机柜内位置", max_length=32, null=True, help_text="机柜内位置")
    last_check = models.DateTimeField("上次检测时间", auto_now=True, help_text="上次检测时间")
    uuid = models.CharField("UUID", max_length=100, db_index=True, null=True, unique=True, help_text="UUID")

    def __str__(self):
        return "{}[{}]".format(self.hostname, self.manage_ip)

    class Meta:
        db_table = 'resources_server'
        ordering = ['id']


class NetworkDevice(models.Model):
    """
    网卡模型
    """
    name = models.CharField("网卡设备名", max_length=32)
    mac = models.CharField("网卡mac地址", max_length=32)
    host = models.ForeignKey(Server, verbose_name="所在服务器")
    remark = models.CharField("备注", max_length=300, null=True)

    def __str__(self):
        return "{}[{}]".format(self.name, self.host)

    class Meta:
        db_table = 'resources_networkdevice'
        ordering = ['id']


class IP(models.Model):
    """
    主机ip地址
    """
    ip_addr = models.CharField("ip地址", max_length=20, db_index=True)
    netmask = models.CharField("子网掩码", max_length=20)
    device = models.ForeignKey(NetworkDevice, verbose_name="网卡")

    def __str__(self):
        return self.ip_addr
        ordering = ['id']

    class Meta:
        db_table = 'resources_ip'
        ordering = ['id']