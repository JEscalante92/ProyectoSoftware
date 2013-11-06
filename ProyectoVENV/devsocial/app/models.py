from django.db import models
from django.contrib.auth.models import User

class tblTipo_evento(models.Model):
	nombre = models.CharField(max_length=140)

	def __unicode__(self):
			return self.nombre
class tblTecnologia(models.Model):
	nombre = models.CharField(max_length=50)
	#fotoPerfil = ProcessedImageField(upload_to='fotoTecnologia',
     #                                      processors=[ResizeToFill(90, 90)],
      #                                     format='JPEG',
       #                                    options={'quality': 60})
	descripcion = models.TextField(max_length=200)

	def __unicode__(self):
		return self.nombre

class tblEvento (models.Model):
	fecha = models.DateField('DD/MM/AAAA')
	titulo = models.CharField(max_length=140)
	organizacion = models.CharField(max_length=140)
	usuario = models.ForeignKey(User)
	tipo_evento = models.ForeignKey(tblTipo_evento)

	def __unicode__ (self):
		return self.titulo

class tblReporte(models.Model):
	tecnologia = models.ForeignKey(tblTecnologia)
	usuario  = models.ForeignKey(User)
	fecha_reporte = models.DateField("DD/MM/AAAA")
	fecha_resuelto = models.DateField("DD/MM/AAAA")
	estado = models.BooleanField()

	def __unicode__ (self):
		return self.fecha_reporte

class tblDenuncia(models.Model):
	moderador = models.ForeignKey(User, related_name='moderador')
	usuario_reportado = models.ForeignKey(User, related_name='usuario_reportado')
	fecha_denuncia = models.DateField('DD/MM/AAAA')
	fecha_resuelto = models.DateField('DD/MM/AAAA')
	estado = models.BooleanField()

	
	#def __unicode__ (self):
	#	return self.get_usuario

class tblHabilidad(models.Model):
	usuario = models.ForeignKey(User)
	tecnologia = models.ForeignKey(tblTecnologia)
	dominio = models.IntegerField(max_length=1)
	def __unicode__ (self):
		return self.tecnologia.nombre

class tblAsignacion_idioma(models.Model):
	idioma = models.CharField(max_length=50)
	usuario = models.ForeignKey(User)
	
class tblProyecto(models.Model):
	habilidad = models.ForeignKey(tblHabilidad)
	usuario = models.ForeignKey(User)
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField(max_length=200)
	fecha = models.DateField('DD/MM/AAAA')
	link_galeria = models.CharField(max_length=50)
	link_proyecto = models.CharField(max_length=50)
	link_organizacion = models.CharField(max_length=50)
	def __unicode__(self):
		return self.nombre
		
class tblUser_profile(models.Model):
	usuario = models.ForeignKey(User)
	#fotoPerfil = ProcessedImageField(upload_to='fotoPerfil',
     #                                      processors=[ResizeToFill(90, 90)],
      #                                     format='JPEG',
       #                                    options={'quality': 60})
	profesion = models.CharField(max_length=50)
	intereses = models.CharField(max_length=50)
	link_Facebook = models.CharField(max_length=50)
	link_Twitter = models.CharField(max_length=50)
	link_GooglePlus = models.CharField(max_length=50)
	link_GitHub = models.CharField(max_length=50)
	link_Web = models.CharField(max_length=50)
	link_Localidad = models.CharField(max_length=50)
	def __unicode__(self):
		return self.profesion