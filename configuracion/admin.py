from django.contrib import admin
from .models import *
from solo.admin import SingletonModelAdmin

# Register your models here.

admin.site.register(Inicio, SingletonModelAdmin)
admin.site.register(Informacion, SingletonModelAdmin)
admin.site.register(Servicios)
admin.site.register(Contacto, SingletonModelAdmin)