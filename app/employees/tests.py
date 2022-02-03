from django.test import TestCase
from employees.models import Employee


class EmployeeTest(TestCase):

    def setUp(self):
        Employee.objects.create(
            first_name='Paul', last_name='brylin', email='paul@dashic.com', phone_number=123222222, clock_in_number=1234
        )

    def test_employee(self):
        first_employee = Employee.objects.get(first_name='Paul')
        self.assertEqual(first_employee.get_employee_first_name(), "Paul")