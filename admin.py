from django.contrib import admin
from .models import РабочееМесто

@admin.register(РабочееМесто)
class РабочееМестоAdmin(admin.ModelAdmin):
    list_display = ('номер_стола', 'сотрудник')
