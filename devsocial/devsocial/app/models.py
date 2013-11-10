from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


EVENTO_CHOICES = (
    ('1', 'Primaria'),
    ('2', 'Nivel Medio'),
    ('3', 'Universidad'),
    
)
class tblTipo_evento(models.Model):
	nombre = models.CharField(max_length=2,choices=EVENTO_CHOICES,blank=False,unique=True)
	def __unicode__(self):
			return self.nombre

class tblTecnologia(models.Model):
	nombre = models.CharField(max_length=50,blank=False,unique=True)
	descripcion = models.TextField(max_length=200,blank=True)
	foto_tecnologia = ProcessedImageField(upload_to='foto_tecnologia',
								default='foto_default/HTML5_Semantics.png',
								processors=[ResizeToFill(90,90)],
								format='JPEG',
								options={'quality':60})
	def __unicode__(self):
		return self.nombre

class tblEvento (models.Model):
	fecha = models.DateField(null=False,blank=False)
	titulo = models.CharField(max_length=140,blank=False)
	organizacion = models.CharField(max_length=140,blank=True)
	usuario = models.ForeignKey(User,blank=False)
	tipo_evento = models.ForeignKey(tblTipo_evento,blank=False)
	def __unicode__ (self):
		return '%s %s' % (self.usuario.username, self.titulo)

class tblReporte(models.Model):
	tecnologia = models.ForeignKey(tblTecnologia,blank=False)
	usuario  = models.ForeignKey(User,blank=False)
	fecha_reporte = models.DateField(null=False,blank=False)
	fecha_resuelto = models.DateField("DD/MM/AAAA",null=True,blank=True)
	estado = models.BooleanField()

	def __unicode__ (self):
		return '%s %s' % (self.usuario.username, self.tecnologia.nombre)

class tblDenuncia(models.Model):
	moderador = models.ForeignKey(User, related_name='moderador',blank=False)
	usuario_reportado = models.ForeignKey(User, related_name='usuario_reportado',blank=False)
	fecha_denuncia = models.DateField(null=False,blank=False)
	fecha_resuelto = models.DateField(blank=True,null=True)
	estado = models.BooleanField()
	def __unicode__ (self):
		return '%s %s' % (self.moderador.username, self.usuario_reportado.username)

class tblHabilidad(models.Model):
	PRINCIPIANTE = 1
	NOVATO = 2
	INTERMEDIO = 3
	AVANZADO = 4
	EXPERTO = 5
	DOMINIO_CHOICES = (
		(PRINCIPIANTE, 'Principiante'),
		(NOVATO, 'Novato'),
		(INTERMEDIO, 'Intermedio'),
		(AVANZADO, 'Avanzado'),
		(EXPERTO, 'Experto'),
	)

	usuario = models.ForeignKey(User,blank=False)
	tecnologia = models.ForeignKey(tblTecnologia,blank=False)
	dominio = models.IntegerField(choices=DOMINIO_CHOICES, default=PRINCIPIANTE)
	def __unicode__ (self):
		return '%s %s' % (self.usuario.username, self.tecnologia.nombre)

class tblAsignacion_idioma(models.Model):
	idioma = models.CharField(max_length=50,blank=False)
	usuario = models.ForeignKey(User,blank=False, related_name='idiomas')
	def __unicode__ (self):
		return '%s %s' % (self.usuario.username, self.idioma)


class tblProyecto(models.Model):
	habilidad = models.ForeignKey(tblHabilidad,blank=False)
	usuario = models.ForeignKey(User,blank=False)
	nombre = models.CharField(max_length=50,blank=False)
	descripcion = models.TextField(max_length=200,blank=False)
	fecha = models.DateField(null=False,blank=False)
	Url_proyecto = models.URLField(blank=True)
	Url_organizacion = models.URLField(blank=True)
	like= models.IntegerField(blank=True,null=True)
	unlike= models.IntegerField(blank=True,null=True)
	def __unicode__(self):
		return '%s %s' % (self.usuario.username, self.nombre) 

class tblGaleria(models.Model):
	foto = ProcessedImageField(upload_to='foto_galeria',
								default='foto_default/Responsive_Device.png',
								processors=[ResizeToFill(90,90)],
								format='JPEG',
								options={'quality':60})
	proyecto = models.ForeignKey(tblProyecto,blank=False)
	def __unicode__ (self):
		return self.proyecto.nombre
	
class tblAsignacion_habilidad(models.Model):
	proyecto = models.ForeignKey(tblProyecto,blank=False)
	habilidad = models.ForeignKey(tblHabilidad,blank=False)
	def __unicode__ (self):
		return '%s %s' % (self.proyecto.nombre, self.habilidad.tecnologia.nombre)

		
class tblUser_profile(models.Model):
	usuario = models.OneToOneField(User,blank=True,unique=True, related_name='perfil')
	foto = ProcessedImageField(upload_to='foto_perfil',
								default='foto_default/user-settings.png',
								processors=[ResizeToFill(90,90)],
								format='JPEG',
								options={'quality':60})
	profesion = models.CharField(max_length=50,blank=True)
	intereses = models.CharField(max_length=140,blank=True)
	link_Facebook = models.URLField(blank=True)
	link_Twitter = models.URLField(blank=True)
	link_GooglePlus = models.URLField(blank=True)
	link_Web = models.URLField(blank=True)
	link_Localidad = models.CharField(max_length=50,blank=True)
	def __unicode__(self):
		return '%s %s' % (self.usuario.username, self.profesion)