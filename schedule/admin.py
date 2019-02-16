# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Medicine
# Register your models here.

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    pass
