# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models

# Create your models here.

class Client(models.Model):
    first = models.CharField(max_length = 50)
    last = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 50)

    def __str__(self):
        #print(dir(self))
        return self.first + ' ' + self.last

class Medicine(models.Model):
    name = models.CharField(max_length = 50)
    timeGap = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(24)])
    num_pill_taken = models.IntegerField(default=0)
    num_pill_missed = models.IntegerField(default = 0)
    container = models.IntegerField(default = 0)
    user_id = models.IntegerField(default = 6)

    def __str__(self):
        #print(Client.objects.filter(pk=self.user_id))
        #return self.name
        return Client.objects.filter(pk=self.user_id).values_list('last', flat = True)[0] + " " + self.name

class Container(models.Model):
    number = models.IntegerField(default=-1)
    busy = models.BooleanField(default=0)
    drug_id = models.IntegerField(default=-1)
    user_id = models.IntegerField(default = 1)

    def __str__(self):
        return Client.objects.filter(pk=self.user_id).values_list('last', flat = True)[0] + " " + str(self.number)

