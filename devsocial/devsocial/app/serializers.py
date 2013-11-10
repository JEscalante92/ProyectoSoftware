# -*- encoding: utf-8 -*-
from rest_framework import serializers

from django.contrib.auth.models import User

from .models import tblUser_profile, tblAsignacion_idioma

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

	class Meta:
		model = User
		fields = ('username','email','first_name','last_name','perfil','idiomas')