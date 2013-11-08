from rest_framework.generics import ListCreateAPIView
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponseRedirect
from .models import *
from .forms import LoginForm

class Tipo_evento(ListCreateAPIView):
	model = tblTipo_evento
	ordering=('-name',)

class Tecnologia(ListCreateAPIView):
	model = tblTecnologia

class Evento (ListCreateAPIView):
	model = tblEvento 

class Reporte(ListCreateAPIView):
	model = tblReporte

class Denuncia(ListCreateAPIView):
	model = tblDenuncia

class Habilidad(ListCreateAPIView):
	model = tblHabilidad

class Asignacion_idioma(ListCreateAPIView):
	model = tblAsignacion_idioma 

class User_profile(ListCreateAPIView):
	model = tblUser_profile

class Galeria(ListCreateAPIView):
	model = tblGaleria

class Asignacion_habilidad(ListCreateAPIView):
	model = tblAsignacion_habilidad

class Proyecto(ListCreateAPIView):
	model = tblProyecto

class Usuario(ListCreateAPIView):
	model = User

def home(request):
	template = "inicio.html"
	return render(request, template)
def ingreso(request):
	template = "login.html"
	if request.method=='POST':
		formulario = LoginForm(request.POST)
		if formulario.is_valid():
			username = formulario.cleaned_data['username']
			password = formulario.cleaned_data['password']
			acceso = auth.authenticate(username=username, password=password)
			if acceso is not None:
				if acceso.is_active:
					auth.login(request, acceso)
					return HttpResponseRedirect('/')
				else:
					return HttpResponseRedirect('/noactivo')
			else:
				return HttpResponseRedirect('/incorrecto')
	else:
		formulario = LoginForm()
	return render_to_response('login.html', {'formulario':formulario}, context_instance=RequestContext(request))
@login_required
def salida(request):
	auth.logout(request)
	return HttpResponseRedirect('/')