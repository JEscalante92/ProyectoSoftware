# -*- encoding: utf-8 -*-
from django.forms import widgets

from rest_framework import serializers

from django.contrib.auth.models import User

from .models import tblUser_profile, tblAsignacion_idioma, tblProyecto, tblGaleria

from app.models import tblTecnologia, tblHabilidad, tblEvento

class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblTecnologia
        fields = ('id','nombre', 'descripcion', 'foto_tecnologia')

class HabilidadSerializer(serializers.ModelSerializer):
	tecnologia = TecnologiaSerializer(many=False)
	class Meta:
		model = tblHabilidad
		fields = ('usuario','dominio','tecnologia')

class LogroSerializer(serializers.ModelSerializer):
	class Meta:
		model = tblEvento
		fields = ('id','fecha','titulo','organizacion','tipo_evento')

class HabilidadEditSerializer(serializers.ModelSerializer):
	class Meta:
		model = tblHabilidad
		fields = ('usuario','dominio','tecnologia')

class User_profileSerializer(serializers.ModelSerializer):
	class Meta:
		model = tblUser_profile
		fields = ('foto','profesion', 'intereses','link_Facebook','link_Twitter', 'link_GooglePlus', 'link_Web', 'link_Localidad')

class IdiomaSerializer(serializers.ModelSerializer):
	class Meta:
		model = tblAsignacion_idioma
		fields = ('idioma',)
class UserSerializer(serializers.ModelSerializer):
	perfil = User_profileSerializer(many=False)
	idiomas = IdiomaSerializer(many=True)
	habilidades = HabilidadSerializer(many=True)
	logros = LogroSerializer(many=True)
	class Meta:
		model = User
		fields = ('username','email','first_name','last_name','perfil','idiomas',)

class TecnologiaUserSerializer(serializers.ModelSerializer):
	usuario = UserSerializer(many=False)
	tecnologia = TecnologiaSerializer(many=False)
	class Meta:
		model = tblHabilidad
		fields = ('usuario','dominio','tecnologia')

class GaleriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = tblGaleria
		fields = ('id','foto')

class ProyectoSerializer(serializers.ModelSerializer):
	proyectos = GaleriaSerializer(many=True)
	class Meta:
		model = tblProyecto
		fields = ('id', 'nombre', 'descripcion', 'fecha', 'Url_proyecto', 'Url_organizacion', 'proyectos')