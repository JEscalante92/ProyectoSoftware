# -*- encoding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Q
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponseRedirect
from .models import *
from .forms import LoginForm,RegistroUserForm,ModificarPerfilForm,RegistroProyectoForm,ModificarProyectoForm,CambiarFotoForm, CambiarLocalidadForm
from .serializers import *
from django.core import serializers
from app.models import tblTecnologia
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

import pygeoip
import re, urllib2
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect
from django.template.response import TemplateResponse
from django.contrib.auth.forms import PasswordChangeForm

"""
Vistas para API REST
"""
class UsersList(APIView):
    def get(self, request, format='json'):
        queryset = User.objects.all()
        username = self.request.QUERY_PARAMS.get('username', None)
        pais = self.request.QUERY_PARAMS.get('pais', None)
        search = self.request.QUERY_PARAMS.get('search', None)
        if username is not None:
            queryset = queryset.filter(username=username)

        if search is not None:
            queryset = queryset.filter(Q(username__istartswith=search) | Q(first_name__istartswith=search))
        
        if pais is not None:
            queryset = queryset.filter(perfil__link_Localidad=pais)
        
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

class ProyectosList(APIView):
    def get(self, request, format='json'):
        username = self.request.QUERY_PARAMS.get('username', None)
        queryset = tblProyecto.objects.all()
        if username is not None:
            try:
                user = User.objects.get(username=username)
                queryset = queryset.filter(usuario=user)
            except User.DoesNotExist:
                queryset = tblProyecto.objects.none()

        serializer = ProyectoSerializer(queryset, many=True)
        return Response(serializer.data)

class TecnologiasList(APIView):
    def get(self, request, format='json'):
        start_index = int(self.request.QUERY_PARAMS.get('start-index', 1))
        get_all = self.request.QUERY_PARAMS.get('get', None)
        if start_index == 0:
            start_index = 1
        queryset = tblTecnologia.objects.all()
        username = self.request.QUERY_PARAMS.get('username', None)
        search = self.request.QUERY_PARAMS.get('search', None)
        tecnologia = self.request.QUERY_PARAMS.get('tecnologia', None)
        if username is not None:
            try:
                user = User.objects.get(username=username)
                queryset = queryset.filter(tecnologia__usuario=user)
            except User.DoesNotExist:
                queryset = tblTecnologia.objects.none()  
        
        if search is not None:
            queryset = tblTecnologia.objects.all().filter(Q(nombre__istartswith=search))[int(start_index)-1 : int(start_index)+4]
        
        if tecnologia is not None:
            queryset = queryset.filter(nombre=tecnologia)

        serializer = TecnologiaSerializer(queryset, many=True)
        return Response(serializer.data)

class LogrosList(APIView):
    def get(self, request, format='json'):
        start_index = int(self.request.QUERY_PARAMS.get('start-index', 1))
        get_all = self.request.QUERY_PARAMS.get('get', None)
        if start_index == 0:
            start_index = 1
        username = self.request.QUERY_PARAMS.get('username', None)
        if username is not None:
            try:
                user = User.objects.get(username=username)
                queryset = tblEvento.objects.all().filter(usuario=user)[int(start_index)-1 : int(start_index)+4]
                if get_all == 'all':
                    queryset = tblEvento.objects.all().filter(usuario=user)
            except User.DoesNotExist:
                queryset = tblEvento.objects.none() 
        else:
            queryset = tblEvento.objects.all()[int(start_index)-1 : int(start_index)+4]
        if get_all == 'all':
            queryset = tblEvento.objects.all()
        serializer = LogroSerializer(queryset, many=True)
        return Response(serializer.data)

class TecnologiaUserList(APIView):
    def get(self , request, format='json'):
        start_index = int(self.request.QUERY_PARAMS.get('start-index', 1))
        get_all = self.request.QUERY_PARAMS.get('get', None)
        tecnologia = self.request.QUERY_PARAMS.get('tecnologia', None)
        if start_index == 0:
            start_index= 1
        username = self.request.QUERY_PARAMS.get('username', None)
        
        if username is not None:
            try:
                user = User.objects.get(username=username)
                queryset = tblHabilidad.objects.all().filter(usuario=user)[int(start_index)-1 : int(start_index)+4]
                if get_all == 'all':
                    queryset = tblHabilidad.objects.all().filter(usuario=user)
            except User.DoesNotExist:
                queryset = tblHabilidad.objects.none() 
        else:
            queryset = tblHabilidad.objects.all()[int(start_index)-1 : int(start_index)+4]
        
        if tecnologia is not None:
            QueryTecnologia = tblTecnologia.objects.all().filter(Q(nombre__istartswith=tecnologia))[0]
            queryset = tblHabilidad.objects.all().filter(tecnologia=QueryTecnologia)[int(start_index)-1 : int(start_index)+4]
        
        if get_all == 'all':
            queryset = tblHabilidad.objects.all()
        serializer = TecnologiaUserSerializer(queryset, many=True)
        return Response(serializer.data)

class HabilidadList(APIView):
    def get(self , request, format='json'):
        start_index = int(self.request.QUERY_PARAMS.get('start-index', 1))
        get_all = self.request.QUERY_PARAMS.get('get', None)
        tecnologia = self.request.QUERY_PARAMS.get('tecnologia', None)
        if start_index == 0:
            start_index= 1
        username = self.request.QUERY_PARAMS.get('username', None)
        
        if username is not None:
            try:
                user = User.objects.get(username=username)
                queryset = tblHabilidad.objects.all().filter(usuario=user)[int(start_index)-1 : int(start_index)+4]
                if get_all == 'all':
                    queryset = tblHabilidad.objects.all().filter(usuario=user)
            except User.DoesNotExist:
                queryset = tblHabilidad.objects.none() 
        else:
            queryset = tblHabilidad.objects.all()[int(start_index)-1 : int(start_index)+4]
        
        if tecnologia is not None:
            QueryTecnologia = tblTecnologia.objects.all().filter(Q(nombre__istartswith=tecnologia))[0]
            queryset = tblHabilidad.objects.all().filter(tecnologia=QueryTecnologia)[int(start_index)-1 : int(start_index)+4]
        
        if get_all == 'all':
            queryset = tblHabilidad.objects.all()
        serializer = HabilidadSerializer(queryset, many=True)
        return Response(serializer.data)

class HabilidadEditList(APIView):
    def get(self, request, format=None):
        habilidades = tblHabilidad.objects.all()
        serializer = HabilidadEditSerializer(habilidades, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if not request.user.is_anonymous():
            habilidad = {'dominio': request.DATA['dominio'], 'tecnologia': request.DATA['tecnologia']} 
            habilidad['usuario'] = request.user.id
            serializer = HabilidadEditSerializer(data=habilidad)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("SESIÓN NO INICIADA", status=status.HTTP_400_BAD_REQUEST)
            
def tperfil(request):
    template = "templates_swig/perfil.html"
    return render(request, template)
def tlogro(request):
    template = "templates_swig/logro.html"
    return render(request, template)
def thabilidad(request):
    template = "templates_swig/habilidad.html"
    return render(request, template)
def ttecnologia(request):
    template = "templates_swig/tecnologia.html"
    return render(request, template)
def tusuario(request):
    template = "templates_swig/usuario.html"
    return render(request, template)
def tusuariosearch(request):
    template = "templates_swig/usuario-search.html"
    return render(request, template)
def ttecnologiasearch(request):
    template = "templates_swig/tecnologia-search.html"
    return render(request, template)
def terror(request):
    template = "templates_swig/error.html"
    return render(request, template)

def home(request):
    if not request.user.is_anonymous():
        url = '/usuarios/%s' % (request.user.username)       
        return HttpResponseRedirect(url)
    template = "inicio.html"
    return render(request, template)

def perfil(request, slug):
    template = "perfil.html"
    return render(request, template)

def modificar(request):
    if request.user.is_anonymous():
        return HttpResponseRedirect('/')
    template = 'modificar.html'
    return render(request, template)

def modificar_personal(request):
    if request.user.is_anonymous():
        return HttpResponseRedirect('/')
    usuario = request.user
    usuarioactual = User.objects.get(id=usuario.id)
    perfil = tblUser_profile.objects.get(id=usuario.id)
    template = 'modificar-personal.html'
    if request.method == 'POST':
        form = ModificarPerfilForm(request.POST,request.FILES)
        if form.is_valid():
            foto = form.cleaned_data['foto']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            profesion = form.cleaned_data['profesion']
            link_Web = form.cleaned_data['link_Web']
            intereses = form.cleaned_data['intereses']
            usuarioactual.first_name = first_name
            usuarioactual.last_name = last_name
            perfil.profesion = profesion
            perfil.link_Web = link_Web
            perfil.intereses = intereses
            usuarioactual.save()
            if foto:
                perfil.foto=foto
            usuarioactual.save()
            perfil.save()  
            return render_to_response('prueba-gracias.html', context_instance=RequestContext(request))
        else:
            return render_to_response(template,{'form':form,'usuario':usuarioactual,'perfil':perfil},context_instance=RequestContext(request))        
    elif request.method == 'GET':
        form = ModificarPerfilForm(initial={
                                    'first_name': usuarioactual.first_name,
                                    'last_name': usuarioactual.last_name,
                                    'profesion':perfil.profesion,
                                    'link_Web':perfil.link_Web,
                                    'intereses':perfil.intereses,
                                    'link_Localidad':perfil.link_Localidad,


            })
    return render_to_response(template,{'form':form,'usuario':usuarioactual,'perfil':perfil},context_instance=RequestContext(request))

def tecnologias(request, slug):
    template = "tecnologias.html"
    return render(request, template)
def search(request):
    template = "busqueda.html"
    return render(request, template)

def ingreso(request):
    template = "login.html"
    if request.method=='POST':
        formulario = LoginForm(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
            acceso = auth.authenticate(username=username, password=password)
            if acceso is not None:
                if acceso.is_active:
                    auth.login(request, acceso)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect('/noactivo')
            else:
                return HttpResponseRedirect('/incorrecto')
    else:
        formulario = LoginForm()
    return render_to_response('login.html', {'formulario':formulario}, context_instance=RequestContext(request))
@login_required
def salida(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

"""
Vistas para Tecnologia
"""
def tecnoNombre(request, **kwargs):
    tecno = tblTecnologia.objects.filter(nombre = kwargs['nombre'])
    serializer = TecnologiaSerializer(tecno, many=True)
    return HttpResponse(serializer.data, mimetype='application/json')

def tecnoUsuario(request, **kwargs):
    persona = User.objects.get(username = kwargs['username'])
    habilidad = tblHabilidad.objects.filter(usuario = persona).order_by('dominio')
    tecno = []
    for i in habilidad:
        tecno.append(tblTecnologia.objects.get(nombre=i))
    serializer = TecnologiaSerializer(tecno, many=True)
    return HttpResponse(serializer.data, mimetype='application/json')

@api_view(['GET', 'POST'])
def tecnoLista(request):
    """
    Lista las tecnologias registradas y registra una nueva tecnologia
    """
    if request.method == 'GET':
        tecno = tblTecnologia.objects.all()
        serializer = TecnologiaSerializer(tecno, many=True)
        return HttpResponse(serializer.data, mimetype='application/json')
    elif request.method == 'POST':
        serializer = TecnologiaSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def registroUsuario(request):
    form = RegistroUserForm()
    if request.method =='POST':
        form = RegistroUserForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            nombres = form.cleaned_data['first_name']
            apellidos = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password_one = form.cleaned_data['password_one']
            password_two = form.cleaned_data['password_two']
            usuariocreate = User.objects.create_user(username=usuario,email=email,first_name=nombres,last_name=apellidos,password=password_one)
            usuariocreate.save()
            perfil = tblUser_profile()
            perfil.usuario = usuariocreate
            perfil.link_Localidad = setip(request)
            perfil.save()
            return render_to_response('prueba-gracias.html', context_instance=RequestContext(request))
        else:
            return render_to_response('prueba_form.html',{'form':form},context_instance=RequestContext(request))
    return render_to_response('prueba_form.html',{'form':form},context_instance=RequestContext(request))

def get_client_ip():
    ip = urllib2.urlopen('http://api.wipmania.com').read()
    ip = re.match(r"(.*)<br>(\w+)", ip)
    return ip.group(1)

def setip(request):
    g = pygeoip.GeoIP('GeoLiteCity.dat')
    localidad = g.country_name_by_addr(get_client_ip())
    return localidad

@login_required
def modificarUsuario(request):
    usuario = request.user
    usuarioactual = User.objects.get(id=usuario.id)
    perfil = tblUser_profile.objects.get(id=usuario.id)
    if request.method == 'POST':
        form = ModificarPerfilForm(request.POST,request.FILES)
        if form.is_valid():
            foto = form.cleaned_data['foto']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            profesion = form.cleaned_data['profesion']
            link_Web = form.cleaned_data['link_Web']
            intereses = form.cleaned_data['intereses']
            link_Localidad = form.cleaned_data['link_Localidad']
            usuarioactual.first_name = first_name
            usuarioactual.last_name = last_name
            perfil.profesion = profesion
            perfil.link_Web = link_Web
            perfil.intereses = intereses
            perfil.link_Localidad = link_Localidad
            usuarioactual.save()
            if foto:
                perfil.foto=foto
            usuarioactual.save()
            perfil.save()  
            perfil.save()  
            return render_to_response('prueba-gracias.html', context_instance=RequestContext(request))
        else:
            return render_to_response('prueba_formfoto.html',{'form':form,'usuario':usuarioactual,'perfil':perfil},context_instance=RequestContext(request))

    elif request.method == 'GET':
        form = ModificarPerfilForm(initial={
                                    'first_name': usuarioactual.first_name,
                                    'last_name': usuarioactual.last_name,
                                    'profesion':perfil.profesion,
                                    'link_Web':perfil.link_Web,
                                    'intereses':perfil.intereses,
                                    'link_Localidad':perfil.link_Localidad,


            })
                
    return render_to_response('prueba_formfoto.html',{'form':form,'usuario':usuarioactual,'perfil':perfil},context_instance=RequestContext(request))
@login_required
def CambiarLocalidad(request):
    usuario = request.user
    usuarioactual = User.objects.get(id=usuario.id)
    perfil = tblUser_profile.objects.get(id=usuario.id)    
    if request.method == "POST":
        form = CambiarLocalidadForm(request.POST)
        if form.is_valid():
            perfil.link_Localidad = setip(request)
            perfil.save();
            return render_to_response('prueba-gracias.html', context_instance=RequestContext(request))
        else:
            return render_to_response('prueba_form.html',{'form':form,'perfil':perfil},context_instance=RequestContext(request))
    
    if request.method =="GET":
        form=CambiarLocalidadForm(initial={
                                'link_Localidad':perfil.link_Localidad
            })
    return render_to_response('prueba_form.html',{'form':form,'perfil':perfil},context_instance=RequestContext(request))
    

@sensitive_post_parameters()
@csrf_protect
@login_required
def CambiarPassword(request,
                    template_name='prueba_form.html',
                    post_change_redirect=None,
                    password_change_form=PasswordChangeForm,
                    ):
    
    if request.method == "POST":
        form = password_change_form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('prueba-gracias.html', context_instance=RequestContext(request))    
    else:
        form = password_change_form(user=request.user)
    return TemplateResponse(request, template_name, {'form': form})

@login_required
def registroProyecto(request):
    usuario = request.user
    usuarioactual = User.objects.get(id=usuario.id)
    form = RegistroProyectoForm()
    if request.method =='POST':
        form = RegistroProyectoForm(request.POST,request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            fecha = form.cleaned_data['fecha']
            descripcion = form.cleaned_data['descripcion']
            foto = form.cleaned_data['foto']
            proyecto= tblProyecto()
            proyecto.usuario= usuarioactual
            proyecto.nombre = nombre
            proyecto.fecha =fecha
            proyecto.descripcion = descripcion
            proyecto.save()
            galeria = tblGaleria()
            if foto:
                galeria.foto = foto
            galeria.proyecto = proyecto
            galeria.save()
            return render_to_response('prueba-gracias.html', context_instance=RequestContext(request))
        else:
            return render_to_response('prueba_form.html',{'form':form},context_instance=RequestContext(request))
    return render_to_response('prueba_form.html',{'form':form},context_instance=RequestContext(request))

@login_required
def ModificarProyecto(request,idproyecto):
    usuario= request.user
    usuarioactual = User.objects.get(id=usuario.id)
    proyecto = tblProyecto.objects.get(id=idproyecto)
    if proyecto.usuario == usuarioactual:
        form = ModificarProyectoForm()
        if request.method =='POST':
            form = ModificarProyectoForm(request.POST)
            if form.is_valid():
                nombre = form.cleaned_data['nombre']
                fecha = form.cleaned_data['fecha']
                descripcion = form.cleaned_data['descripcion']
                url_proyecto = form.cleaned_data['url_proyecto']
                url_organizacion = form.cleaned_data['url_organizacion']
                
                proyecto.nombre = nombre
                proyecto.fecha =fecha
                proyecto.descripcion = descripcion
                proyecto.Url_proyecto=url_proyecto
                proyecto.Url_organizacion = url_organizacion
                proyecto.save()
                return render_to_response('prueba-gracias.html', context_instance=RequestContext(request))
            else:
                return render_to_response('prueba_form.html',{'form':form},context_instance=RequestContext(request))
        elif request.method == 'GET':
            
            form = ModificarProyectoForm(initial={
                                        'nombre':proyecto.nombre,
                                        'fecha':proyecto.fecha,
                                        'descripcion':proyecto.descripcion,
                                        'url_proyecto':proyecto.Url_proyecto,
                                        'url_organizacion':proyecto.Url_organizacion,
                })        
        return render_to_response('prueba_form.html',{'form':form},context_instance=RequestContext(request))
@login_required
def ModificarFoto(request):
    usuario= request.user
    usuarioactual = User.objects.get(id=usuario.id)
    perfil = tblUser_profile.objects.get(id=usuario.id)
    form = CambiarFotoForm()
    if request.method =='POST':
        form = CambiarFotoForm(request.POST, request.FILES)
        if form.is_valid():    
            foto = form.cleaned_data['foto']
            print (foto)
            if foto:
                perfil.foto = foto
            perfil.save()
            return render_to_response('prueba-gracias.html', context_instance=RequestContext(request))
        else:
            return render_to_response('prueba_formfoto.html',{'form':form},context_instance=RequestContext(request))
           
    return render_to_response('prueba_formfoto.html',{'form':form,'perfil':perfil},context_instance=RequestContext(request))

@login_required
def AgregarGaleriaProyecto(request,idproyecto):
    usuario= request.user
    usuarioactual = User.objects.get(id=usuario.id)
    proyecto = tblProyecto.objects.get(id=idproyecto)
    if proyecto.usuario == usuarioactual:
        form = CambiarFotoForm()
        if request.method =='POST':
            form = CambiarFotoForm(request.POST,request.FILES)
            if form.is_valid():
                foto = form.cleaned_data['foto']
                galeria = tblGaleria()
                if foto:
                    galeria.foto = foto
                    galeria.proyecto = proyecto
                    return render_to_response('prueba-gracias.html', context_instance=RequestContext(request))
            else:
                return render_to_response('prueba_formfoto.html',{'form':form},context_instance=RequestContext(request))
        return render_to_response('prueba_formfoto.html',{'form':form},context_instance=RequestContext(request))

@login_required
def ingresoEvento(request):
    template = "eventos.html"
    form = RegistroEventoForm()
    persona = request.user
    if request.method =='POST':
        form = RegistroEventoForm(request.POST)
        if form.is_valid():
            fecha = form.cleaned_data['fecha']
            titulo = form.cleaned_data['titulo']
            organizacion = form.cleaned_data['organizacion']
            tipo_evento = form.cleaned_data['tipo_evento']
            evento = tblEvento()
            evento.usuario=User.objects.get(id=persona.id)
            evento.fecha=fecha
            evento.titulo=titulo
            evento.organizacion=organizacion
            evento.tipo_evento=tipo_evento
            evento.save()
            return render_to_response('prueba-gracias.html', context_instance=RequestContext(request))
        else:
            return render_to_response('eventos.html', {'form':form},context_instance=RequestContext(request))
    return render_to_response('eventos.html', {'form':form}, context_instance=RequestContext(request))

@login_required
def modificacionEventos(request,idEvento):
    usuario= request.user
    usuarioactual = User.objects.get(id=usuario.id)
    evento = tblEvento.objects.get(id=idEvento)
    if evento.usuario == usuarioactual:
        form = EventoForm()
        if request.method =='POST':
            form = EventoForm(request.POST)
            if form.is_valid():
                fecha = form.cleaned_data['fecha']
                titulo = form.cleaned_data['titulo']
                organizacion = form.cleaned_data['organizacion']
                tipo_evento = form.cleaned_data['tipo_evento']
                
                evento.titulo = titulo
                evento.fecha =fecha
                evento.organizacion = organizacion
                evento.tipo_evento=tipo_evento
                evento.save()
                return render_to_response('prueba-gracias.html', context_instance=RequestContext(request))
            else:
                return render_to_response('eventos.html',{'form':form},context_instance=RequestContext(request))
        elif request.method == 'GET':
            
            form = EventoForm(initial={'titulo':evento.titulo,
                                        'fecha':evento.fecha,
                                        'organizacion':evento.organizacion,
                                        'tipo_evento':evento.tipo_evento,})        
        return render_to_response('eventos.html',{'form':form},context_instance=RequestContext(request))