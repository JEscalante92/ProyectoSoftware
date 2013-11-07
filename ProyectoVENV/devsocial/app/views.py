from rest_framework.generics import ListCreateAPIView
from django.contrib.auth.models import User
from .models import tblTipo_evento, tblTecnologia,tblEvento, tblReporte,tblDenuncia, tblHabilidad,tblAsignacion_idioma, tblUser_profile, tblProyecto

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

class Proyecto(ListCreateAPIView):
	model = tblProyecto

class Usuario(ListCreateAPIView):
	model = User
	