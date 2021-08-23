from django.shortcuts import render
from .models import *
from configuracion.models import *

# Create your views here.
def index(request, template = 'index.html'):
    servicios = Servicios.objects.all()
    return render(request, template, locals())
