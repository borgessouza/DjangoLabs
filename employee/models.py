# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('create_date',)
