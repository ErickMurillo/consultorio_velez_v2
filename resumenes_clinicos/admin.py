from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'edad', 'sexo', 'fecha_ingreso', 'ver_consultas']
    list_filter = ('sexo',)
    search_fields = ['nombre']

    def ver_consultas(self, obj):
        return format_html("<a href='/detalle-consultas/{0}/'>Ver</a>", obj.id)
    ver_consultas.short_description = 'Detalle de consultas'

class ConsultaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['paciente']
    search_fields = ['paciente__nombre']
    list_display = ['paciente', 'motivo_consulta', 'fecha_consulta', 'fecha_prox_consulta']

admin.site.register(Paciente,PacienteAdmin)
admin.site.register(Consulta,ConsultaAdmin)