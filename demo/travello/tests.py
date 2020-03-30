import json
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status


class getTestCase(TestCase):

    def test_getData(self):
        response = self.client.get('/travello/getAll')
        self.assertEqual(response.status_code, status.HTTP_200_OK)