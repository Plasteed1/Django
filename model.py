from django.db import models
import datetime


class EmployeeImage(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='employee_images/')

    def __str__(self):
        return f"Image for {self.employee.first_name} {self.employee.last_name}"


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender_choices = [('M', 'Мужской'), ('F', 'Женский')]
    gender = models.CharField(max_length=1, choices=gender_choices)
    skills = models.JSONField()
    start_date = models.DateField(null=True, blank=True)
    desk_number = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def experience_days(self):
        if self.start_date:
            return (datetime.date.today() - self.start_date).days
        return None

    def clean(self):
        validate_desk_neighbors(self)
