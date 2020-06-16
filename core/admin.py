from django.contrib import admin
from core.models import  Evento
# Register your models here.

class Evento_admin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario', 'data_evento', 'titulo',)

admin.site.register(Evento, Evento_admin)

