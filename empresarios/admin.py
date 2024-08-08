from django.contrib import admin

from .models import Empresas


@admin.register(Empresas)
class EmpresasAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'nome',
        'cnpj',
        'site',
    ]
