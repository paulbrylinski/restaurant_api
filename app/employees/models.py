from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=70, blank=False, default='')
    last_name = models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=50, blank=False, default='')
    phone_number = models.CharField(max_length=12, blank=True, default='')
    clock_in_number = models.IntegerField(blank=False, default='', unique=True)

    def __str__(self):
        return self.first_name