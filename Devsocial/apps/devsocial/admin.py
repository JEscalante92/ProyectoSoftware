from django.contrib import admin
from .models import tblTipo_evento, tblEvento,tblTecnologia, tblReporte, tblDenuncia, tblHabilidad, tblIdiomas, tblAsignacion_idioma, tblProyecto, tblUser_profile

admin.site.register(tblEvento)
admin.site.register(tblTipo_evento)
admin.site.register(tblTecnologia)
admin.site.register(tblReporte)
admin.site.register(tblDenuncia)
admin.site.register(tblHabilidad)
admin.site.register(tblIdiomas)
admin.site.register(tblAsignacion_idioma)
admin.site.register(tblProyecto)
admin.site.register(tblUser_profile)