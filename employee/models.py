# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True, null=True)

