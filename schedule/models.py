# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Medicine(models.Model):
    name = models.CharField(max_length = 50)
    timeGap = models.IntegerField()
    number = models.CharField(max_length = 20)

    def __str__(self):
        return self.name + " Time Gap: " + str(self.timeGap)
