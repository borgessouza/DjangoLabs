# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Employee

# Resister Employee model in django admin
admin.site.register(Employee)
