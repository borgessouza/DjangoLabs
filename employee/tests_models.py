# -*- coding: utf-8 -*-
from django.test import TestCase
from employee.models import Employee

# Create your tests here.
class employee_test_case(TestCase):

    def setUp(self):
        Employee.objects.create(first_name='Ned',
                                last_name='Stark',
                                department='King of North',
                                email='games@thones.com')

        Employee.objects.create(first_name='Robert',
                                last_name='Baratheon',
                                department='King of the Kings',
                                email='games@thones.com')

    def test_departament_case(self):
        ned = Employee.objects.get(first_name="Ned", last_name="Stark")
        self.assertEqual(ned.department, "King of North")

