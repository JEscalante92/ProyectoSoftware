from django import forms
# -*- encoding: utf-8 -*-
class LoginForm(forms.Form):
	username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))