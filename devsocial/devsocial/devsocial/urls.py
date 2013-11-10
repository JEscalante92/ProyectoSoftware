# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from app.views import *
from app import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^registro/$', 'app.views.home', name='home'),
    url(r'^login/$', 'app.views.ingreso', name='ingreso'),
    url(r'^logout/$', 'app.views.salida', name='salida'),
    url(r'^ayuda/$', 'app.views.ingreso', name='ingreso'),
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
    url(r'^Galeria/$', Galeria.as_view(), name='Galeria_Proyecto'),
    url(r'^Asignacion_habilidad/$', Asignacion_habilidad.as_view(), name='Asignacion_habilidad'),
    
    url(r'^usuarios/$', views.UsersList.as_view()),
)