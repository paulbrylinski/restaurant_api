from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeTestCase(APITestCase):
    def test_employee(self):
        data = {"first_name": "Paul"}
        response = self.client.post("/api/employees/<int:pk>/", data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

# Create your tests here.
