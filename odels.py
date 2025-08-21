from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender_choices = [('M', 'Мужской'), ('F', 'Женский')]
    gender = models.CharField(max_length=1, choices=gender_choices)
    skills = models.TextField(help_text='Навыки и уровни освоения')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class EmployeeImage(models.Model):
    employee = models.ForeignKey(Employee, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='employee_images/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
