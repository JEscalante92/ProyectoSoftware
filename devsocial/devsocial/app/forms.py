from django import forms
# -*- encoding: utf-8 -*-
class LoginForm(forms.Form):
	username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

class RegistroUserForm(forms.Form):	
	username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'usuario'}) )
	email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Correo'}) )
	password_one = forms.CharField(label='', widget=forms.PasswordInput(render_value=False,attrs={'placeholder': 'Contrasena'}) )
	password_two = forms.CharField(label='', widget=forms.PasswordInput(render_value=False,attrs={'placeholder': 'Confirmar Contrasena'}) )
	link_Localidad = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Localidad','readonly':True}) )
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
	email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Correo o email'}) )
	profesion = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Profesion'}) )
	link_Web = forms.URLField(label='', widget=forms.TextInput(attrs={'placeholder': 'Sitio Web'}) )
	intereses = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'intereses'}) )
	
	link_Localidad = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Localidad','readonly':True}) )
	
	

	#def clean_email(self):				
	#	email = self.cleaned_data['email']
	#	emailactual = request.COOKIES['email']

	#	if email == self.emailactual:
	#		pass
	#	else:
	#		try:
	#			u = User.objects.get(email=email)
	#		except User.DoesNotExist:
	#			return email
	#		raise forms.ValidationError('Email ya existe para otro usuario')

class CambiarPassForm(forms.Form):	
	password_old = forms.CharField(label='', widget=forms.PasswordInput(render_value=False,attrs={'placeholder': 'Contrasena actual'}) )
	password_one = forms.CharField(label='', widget=forms.PasswordInput(render_value=False,attrs={'placeholder': 'Contrasena nueva'}) )
	password_two = forms.CharField(label='', widget=forms.PasswordInput(render_value=False,attrs={'placeholder': 'Confirmar Contrasena nueva'}) )
		# verificar si pass actual ingreso es igual al del sistema
	
	#def clean_password_old(self):
	#	password_old= self.cleaned_data['password_old']
	#	usuarioactual = User()
    #	usuarioactual = request.user
    #	password = usuarioactual.password
    #	if password_old == password:
	#		pass
     #   else:
	#		raise forms.ValidationError('el password actual no coiciden con el del sistema')
		
	# validar los password nuevos, para ver si conciden
	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('los password nuevos no coiciden')

				