# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Medicine, Container, Client
# Register your models here.

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    pass

@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    pass

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass
