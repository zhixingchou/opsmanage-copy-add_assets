# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Assets(models.Model):
    assets_type_choices = (
        ('server',u'服务器'),
        ('switch',u'交换机'),
    )
    assets_type = models.CharField(choices=assets_type_choices,max_length=100,default='server',verbose_name='资产类型')
    management_ip = models.GenericIPAddressField(u'管理IP',blank=True,null=True)

    class Meta:
        db_table = 'opsmanage_assets'
        permissions = (
            ("can_read_assets","读取资产权限"),
            ("can_change_assets","更改资产权限"),
            ("can_add_assets","添加资产权限"),
            ("can_delete_assets","删除资产权限"),
        )
        verbose_name = '总资产表'
        verbose_name_plural = '总资产表'


class Server_Assets(models.Model):
    assets = models.OneToOneField('Assets')
    ip = models.CharField(max_length=100,unique=True,blank=True,null=True)
    hostname = models.CharField(max_length=100,blank=True,null=True)
    username = models.CharField(max_length=100,blank=True,null=True)
    passwd = models.CharField(max_length=100,blank=True,null=True)
    keyfile = models.SmallIntegerField(blank=True,null=True)
    port = models.DecimalField(max_digits=6,decimal_places=0,blank=True,null=True)
    # kernel = models.CharField(max_length=100,blank=True,null=True)
    cpu = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'opsmanage_server_assets'
        permissions = (
            ("can_read_server_assets", "读取服务器资产权限"),
            ("can_change_server_assets", "更改服务器资产权限"),
            ("can_add_server_assets","添加服务器资产权限"),
            ("can_delete_server_assets","删除服务器资产权限"),
        )
        verbose_name = '服务器资产表'
        verbose_name_plural = '服务器资产表'
