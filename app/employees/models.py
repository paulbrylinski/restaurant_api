from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=70, default='First', blank=False)
    last_name = models.CharField(max_length=70, default='last', blank=False)
    email = models.CharField(max_length=50, default='email@email.com', blank=False)
    phone_number = models.CharField(max_length=12, default=3333333333, blank=True)
    clock_in_number = models.IntegerField(blank=False, default=1234, unique=True)


    def __str__(self):
        return self.first_name

    def get_employee_first_name(self):
        return self.first_name
