# coding:utf-8

from rest_framework import serializers
from appone.models import *
from django.contrib.auth.models import Group,User


class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = ('id','assets_type','management_ip')


class ServerSerializer(serializers.ModelSerializer):
    assets = AssetsSerializer(required=False)
    class Meta:
        model = Server_Assets
        fields = ('id','ip','hostname','username','port','passwd','cpu','assets')

    def create(self, data):
        if(data.get('assets')):
            assets_data = data.pop('assets')
            assets = Assets.objects.create(**assets_data)
        else:
            assets = Assets()
        data['assets'] = assets;
        server = Server_Assets.objects.create(**data)
        return server