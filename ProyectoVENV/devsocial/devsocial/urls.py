from django.conf.urls import patterns, include, url
from app.views import Tipo_evento,Tecnologia,Evento,Reporte,Denuncia, Habilidad,Asignacion_idioma, User_profile, Proyecto,Usuario

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'devsocial.views.home', name='home'),
    # url(r'^devsocial/', include('devsocial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Tipo_evento/$', Tipo_evento.as_view(), name='Tipo_evento'),
    url(r'^Tecnologia/$', Tecnologia.as_view(), name='Tecnologia'),
    url(r'^Evento/$', Evento.as_view(), name='Evento'),
    url(r'^Reporte/$', Reporte.as_view(), name='Reporte'),
    url(r'^Denuncia/$', Denuncia.as_view(), name='Denuncia'),
    url(r'^Habilidad/$', Habilidad.as_view(), name='Habilidad'),
    url(r'^Asignacion_idioma/$', Asignacion_idioma.as_view(), name='Asignacion_idioma'),
    url(r'^User_profile/$', User_profile.as_view(), name='User_profile'),
    url(r'^Proyecto/$', Proyecto.as_view(), name='Proyecto'),
    url(r'^Usuario/$', Usuario.as_view(), name='Usuario'),
    
)
