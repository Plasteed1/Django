from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Навык(models.Model):
    название = models.CharField(max_length=100)

    def __str__(self):
        return self.название


class Сотрудник(models.Model):
    пользователь = models.OneToOneField('сотрудники.User', on_delete=models.CASCADE)
    имя = models.CharField(max_length=50)
    фамилия = models.CharField(max_length=50)
    отчество = models.CharField(max_length=50, blank=True, null=True)
    навыки = models.ManyToManyField(Навык, through='НавыкУровень')


class НавыкУровень(models.Model):
    сотрудник = models.ForeignKey(Сотрудник, on_delete=models.CASCADE)
    навык = models.ForeignKey(Навык, on_delete=models.CASCADE)

    уровень = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)])

    описание = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.сотрудник} - {self.навык} (Уровень: {self.уровень})"
