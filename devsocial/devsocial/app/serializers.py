# -*- encoding: utf-8 -*-
from django.forms import widgets

from rest_framework import serializers

from django.contrib.auth.models import User

from .models import tblUser_profile, tblAsignacion_idioma

from app.models import tblTecnologia, tblHabilidad

class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblTecnologia
        fields = ('id','nombre', 'descripcion', 'foto_tecnologia')

class HabilidadSerializer(serializers.ModelSerializer):
	tecnologia = TecnologiaSerializer(many=False)
	class Meta:
		model = tblHabilidad
		fields = ('usuario','dominio','tecnologia')

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
	class Meta:
		model = User
		fields = ('id','username','email','first_name','last_name','perfil','idiomas','habilidades')