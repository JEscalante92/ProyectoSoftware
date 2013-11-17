from django import forms
# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from datetime import datetime
class LoginForm(forms.Form):
	username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

class RegistroUserForm(forms.Form):	
	username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'usuario'}) )
	email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Correo'}) )
	password_one = forms.CharField(label='', widget=forms.PasswordInput(render_value=False,attrs={'placeholder': 'Contraseña'}) )
	password_two = forms.CharField(label='', widget=forms.PasswordInput(render_value=False,attrs={'placeholder': 'Confirmar Contraseña'}) )
	profesion = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Profesion'}) )
	# verificar si el usuario no ha sido utilizado o registrador anteriormente
	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de Usuario ya existe')
	#verificar si el email no ha sino registrador anteriormente
	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email ya existe')
	
	# validar los password para ver si conciden
	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('los password no coiciden')
class ModificarPerfilForm(forms.Form):	
	first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Nombres'}) )
	last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Apellidos'}) )
	profesion = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Profesion'}) )
	link_Web = forms.URLField(label='', widget=forms.TextInput(attrs={'placeholder': 'Sitio Web'}) )
	intereses = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'intereses'}) )
	link_Localidad = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Localidad','readonly':True}) )
	
class RegistroProyectoForm(forms.Form):	
	nombre = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Nombre proyecto'}) )
	fecha = forms.DateField(label='', widget=forms.DateInput(attrs={'type':'date'})) 
	descripcion = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'descripcion'}) )
	
	

class ModificarProyectoForm(forms.Form):	
	nombre = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Nombre proyecto'}) )
	fecha = forms.DateField(label='', widget=forms.DateInput(attrs={'type': 'date'}) )
	descripcion = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'descripcion'}) )
	url_proyecto = forms.URLField(label='', widget=forms.TextInput(attrs={'placeholder': 'Sitio Web proyecto'}) )
	url_organizacion = forms.URLField(label='', widget=forms.TextInput(attrs={'placeholder': 'Sitio Web organizacion'}) )
	