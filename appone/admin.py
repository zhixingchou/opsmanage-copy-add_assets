# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Assets, Server_Assets

# Register your models here.

admin.site.register(Assets)
admin.site.register(Server_Assets)
