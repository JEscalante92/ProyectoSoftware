# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from app.views import *
from app import views
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^registro/$', 'app.views.home', name='home'),
    url(r'^login/$', 'app.views.ingreso', name='ingreso'),
    url(r'^logout/$', 'app.views.salida', name='salida'),
    url(r'^modificar/personal$', 'app.views.modificar_personal', name='modificar_personal'),
    url(r'^modificar/logros$', 'app.views.modificar_logros', name='modificar_logros'),
    url(r'^modificar/habilidades$', 'app.views.edit_Habilidades', name='edit_Habilidades'),
    url(r'^modificar/portafolio$', 'app.views.portafolio', name='portafolio'),
   #url(r'^modificar/ip$', 'app.views.modificar_ip', name='modificar_ip'),
    url(r'^modificar/contrasenna$', 'app.views.modificar_contrasenna', name='modificar_contrasenna'),
    url(r'^ayuda/$', 'app.views.ayuda', name='ingreso'),
    
    #Logros:
    url(r'^modificar/nuevologro$', 'app.views.nuevologro', name='nuevologro'),
    
    url(r'^usuarios/(?P<slug>[-\w]+)/$', 'app.views.perfil', name='perfil'),
    url(r'^tecnologias/(?P<slug>[-\w]+)/$', 'app.views.tecnologias', name='tecnologias'),
    url(r'^search/$', 'app.views.search', name='search'),
    # url(r'^$', 'devsocial.views.home', name='home'),
    # url(r'^devsocial/', include('devsocial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #Templates - solicitudes AJAX
    url(r'^templates/perfil$', 'app.views.tperfil', name='tperfil'),
    url(r'^templates/logro$', 'app.views.tlogro', name='tlogro'),
    url(r'^templates/logro-edit$', 'app.views.tlogro_edit', name='tlogro_edit'),
    url(r'^templates/habilidad$', 'app.views.thabilidad', name='thabilidad'),
    url(r'^templates/tecnologia$', 'app.views.ttecnologia', name='ttecnologia'),
    url(r'^templates/usuario$', 'app.views.tusuario', name='tusuario'),
    url(r'^templates/usuario-search$', 'app.views.tusuariosearch', name='tusuariosearch'),
    url(r'^templates/tecnologia-search$', 'app.views.ttecnologiasearch', name='ttecnologiasearch'),
    url(r'^templates/error$', 'app.views.terror', name='terror'),
    
    #API - rutas para los datos
    url(r'^api/usuarios/$', views.UsersList.as_view()),
    url(r'^api/tecnologias/$', views.TecnologiasList.as_view()),
    url(r'^api/habilidad/$', views.HabilidadList.as_view()),
    url(r'^api/tecnologia-user/$', views.TecnologiaUserList.as_view()),
    url(r'^api/logros/$', views.LogrosList.as_view()),
    url(r'^api/proyectos/$', views.ProyectosList.as_view()),
    url(r'^api/ipedit/$', views.ipEdit.as_view()),

    url(r'^tecnoLista/$', 'tecnoLista', name='tecnoLista'),#retorna una lista con todas las tecnologias registradas
    url(r'^tecnoUsuario/(?P<username>[a-zA-Z0-9\s\+]+)$', 'tecnoUsuario', name='tecnoUsuario'),#con el username da las tecnologias que tiene
    url(r'^tecnoNombre/(?P<nombre>[a-zA-Z0-9\s\+]+)$', 'tecnoNombre', name='tecnoNombre'),#en el nombre da los datos de la tecnologia
)
# servidores de medios para acceder a las imagenes.
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    )   
# url para pruebas
urlpatterns += patterns('',
    url(r'', include('social_auth.urls')),
        
    url(r'^usuario/registrarse/twitter$', 'app.views.registroUsuarioSocial',name='registrase'),
    url(r'^usuario/registrarse/$', 'app.views.registroUsuario',name='registrase'),
   
    #url(r'^usuario/modificar/$', 'app.views.modificarUsuario',name='registrase'),
    url(r'^usuario/cambiar_password/$', 'app.views.CambiarPassword',name='registrase'),
    url(r'^proyecto/registrar/$', 'app.views.registroProyecto',name='registrase'),
    url(r'^proyecto/modificar/(?P<idproyecto>[a-zA-Z0-9\s\+]+)$', 'app.views.ModificarProyecto',name='registrase'),
    url(r'^proyecto/galeria/(?P<idproyecto>[a-zA-Z0-9\s\+]+)$', 'app.views.AgregarGaleriaProyecto',name='registrase'),
    #url(r'^usuario/cambiar_localidad/$', 'app.views.CambiarLocalidad',name='cambiar localidad'),
    
    url(r'^cambiar_foto/$', 'app.views.ModificarFoto',name='foto'),
)       
