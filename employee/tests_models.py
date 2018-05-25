# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Employee

# Create your tests here.
class employee_test_case(TestCase):
    def setUp(self):
        Employee.objects.create(first_name='Ned', last_name='Stark', department='King of North')
        Employee.objects.create(first_name='Robert', last_name='Baratheon', department='King of the Kings')

    def test_departament_case(self):
        ned = Employee.objects.get(first_name="Ned", last_name="Stark")
        self.assertEqual(ned.department, "King of North")
