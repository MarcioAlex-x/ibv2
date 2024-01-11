from django.contrib import admin
from .models import Destaque, Publicacoes, Programacao, Eventos, Classificados

admin.site.register(Destaque)
admin.site.register(Publicacoes)
admin.site.register(Programacao)
admin.site.register(Eventos)
admin.site.register(Classificados)

# Register your models here.
