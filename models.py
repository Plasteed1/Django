from django.db import models
from сотрудники.models import Сотрудник


class РабочееМесто(models.Model):
    номер_стола = models.CharField(max_length=10)
    дополнительная_информация = models.TextField(blank=True, null=True)

    сотрудник = models.OneToOneField(Сотрудник, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Стол {self.номер_стола}"
