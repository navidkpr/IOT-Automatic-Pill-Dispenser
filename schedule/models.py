# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models

# Create your models here.

class Medicine(models.Model):
    name = models.CharField(max_length = 50)
    timeGap = models.IntegerField(validators = [MinValueValidator(4), MaxValueValidator(24)])
    num_pill_taken = models.IntegerField(default=0)
    num_pill_missed = models.IntegerField(default = 0)

    def __str__(self):
        return self.name + " Time Gap: " + str(self.timeGap)
