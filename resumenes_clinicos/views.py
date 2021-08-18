from django.shortcuts import render
from .models import *

# Create your views here.
def index(request, template = 'index.html'):
    return render(request, template, locals())
