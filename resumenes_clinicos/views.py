from django.shortcuts import render
from .models import *
from configuracion.models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages

# Create your views here.
def index(request, template = 'index.html'):
	servicios = Servicios.objects.all()
	if request.method == 'POST':
		form = ContactoForm(request.POST)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			telefono = form.cleaned_data['telefono']
			mensaje = form.cleaned_data['mensaje']

			# try:
			subject, from_email = 'Correo de DrVelezPonce.com', 'juancarlos@drvelezponce.com'
			text_content =  render_to_string('correo.txt', {'nombre': nombre, 'telefono':telefono, 'mensaje':mensaje})

			html_content = render_to_string('correo.txt', {'nombre': nombre, 'telefono':telefono, 'mensaje':mensaje})

			msg = EmailMultiAlternatives(subject, text_content, from_email, ['juancarlos@drvelezponce.com',])
			msg.attach_alternative(html_content, "text/html")
			msg.send()

			enviado = True
			messages.success(request, 'Success!')
			return HttpResponseRedirect(request.path)
			# except:
			# 	pass
	else:
		form = ContactoForm()
		
	return render(request, template, locals())

def detalle_consultas(request,template='detalle_consulta.html',id=None):
	paciente = Paciente.objects.get(id = id)
	consultas = Consulta.objects.filter(paciente = id)
	return render(request, template, locals())
