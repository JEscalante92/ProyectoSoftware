from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class tblTipo_evento(models.Model):
	nombre = models.CharField(max_length=140)
	def __unicode__(self):
			return self.nombre

class tblTecnologia(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField(max_length=200)
	foto_tecnologia = ProcessedImageField(upload_to='foto_tecnologia',
								processors=[ResizeToFill(90,90)],
								format='JPEG',
								options={'quality':60})
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
		return self.usuario.username

class tblDenuncia(models.Model):
	moderador = models.ForeignKey(User, related_name='moderador')
	usuario_reportado = models.ForeignKey(User, related_name='usuario_reportado')
	fecha_denuncia = models.DateField('DD/MM/AAAA')
	fecha_resuelto = models.DateField('DD/MM/AAAA')
	estado = models.BooleanField()
	def __unicode__ (self):
		return self.usuario_reportado.username


DOMINIO_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)
class tblHabilidad(models.Model):
	usuario = models.ForeignKey(User)
	tecnologia = models.ForeignKey(tblTecnologia)
	dominio = models.CharField(max_length=1, choices=DOMINIO_CHOICES)
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
	Url_galeria = models.URLField()
	Url_proyecto = models.URLField()
	Url_organizacion = models.URLField()
	def __unicode__(self):
		return self.nombre
		
class tblUser_profile(models.Model):
	usuario = models.ForeignKey(User)
	foto = ProcessedImageField(upload_to='foto_perfil',
								processors=[ResizeToFill(90,90)],
								format='JPEG',
								options={'quality':60})
	profesion = models.CharField(max_length=50)
	intereses = models.CharField(max_length=50)
	link_Facebook = models.URLField()
	link_Twitter = models.URLField()
	link_GooglePlus = models.URLField()
	link_GitHub = models.URLField()
	link_Web = models.URLField()
	link_Localidad = models.CharField(max_length=50)
	def __unicode__(self):
		return self.usuario.username