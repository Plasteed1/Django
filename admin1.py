from django.contrib import admin
from .models import Сотрудник, Навык, НавыкУровень

@admin.register(Сотрудник)
class СотрудникAdmin(admin.ModelAdmin):
    list_display = ('имя', 'фамилия', 'отчество')

@admin.register(Навык)
class НавыкAdmin(admin.ModelAdmin):
    pass

@admin.register(НавыкУровень)
class НавыкУровеньAdmin(admin.ModelAdmin):
    list_display = ('сотрудник', 'навык', 'уровень')
