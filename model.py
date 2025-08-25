from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    pass
class Employee(models.Model):
    name = models.CharField(max_length=255)
    skills = models.TextField()
    experience_years = models.PositiveIntegerField()
    table_number = models.PositiveIntegerField()
    def __str__(self):
        return self.name
