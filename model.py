from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
class Collect(models.Model):
    CATEGORY_CHOICES = [
        ('birthday', "День рождения"),
        ('wedding', "Свадьба"),
        ('other', "Другое"),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collects')
    title = models.CharField(max_length=255)
    reason = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    target_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True,
                                        blank=True)
    current_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Payment(models.Model):
    collect = models.ForeignKey(Collect, on_delete=models.CASCADE, related_name='payments')
    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)
