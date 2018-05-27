# -*- coding: utf-8 -*-

import unittest
import json
from django.test import TestCase


class test_employee_view(TestCase):

    def test_list_employee(self):
        response = self.client.get('/employee/')
        self.assertEqual(response.status_code, 200)


    def test_add_employee(self):
        employee_test = {
            'first_name': 'Tyrion',
            'last_name' : 'Lannister',
            'department': 'Small of Lannister',
            'email'     : 'games@thones.com'
        }

        response = self.client.post('/employee/',
                                    json.dumps(employee_test),
                                    content_type="application/json")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['first_name'], 'Tyrion' )

    def test_update_employee(self):
        employee = {
            'first_name': 'Cersei',
            'last_name' : 'Lannister',
            'department': 'Queen',
            'email'     : 'games@thones.com'
        }

        response = self.client.post('/employee/',
                                    json.dumps(employee),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 201)

        url = '/employee/{}/'.format(response.json()['id'])
        employee['department']='Mad Queen'

        response = self.client.put(url,
                                   json.dumps(employee),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['department'], 'Mad Queen')


    def test_delete_employee(self):
        employee = {
            'first_name': 'Tywin',
            'last_name' : 'Lannister',
            'department': 'King Lannister',
            'email'     : 'games@thones.com'
        }

        response = self.client.post('/employee/',
                                json.dumps(employee),
                                content_type='application/json')

        self.assertEqual(response.status_code, 201)

        url = '/employee/{}/'.format(response.json()['id'])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)


    def test_not_found_employee(self):
        response = self.client.get('/employee/20/')
        self.assertEqual(response.status_code, 404)



    def test_not_valid_employee(self):
        employee_test = {
            'last_name' : 'Lannister',
            'department': 'Small of Lannister',
            'email'     : 'games@thones.com'
        }

        response = self.client.post('/employee/',
                                json.dumps(employee_test),
                                content_type="application/json")

        self.assertEqual(response.status_code,400)

        employee_test = {
            'first_name': 'Tywin',
            'last_name' : 'Lannister',
            'department': 'King Lannister'
        }

        response = self.client.post('/employee/',
                                    json.dumps(employee_test),
                                    content_type="application/json")

        self.assertEqual(response.status_code,400)


