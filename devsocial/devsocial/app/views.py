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
from .forms import LoginForm
from .serializers import UserSerializer
from .filters import UserFilter
from app.serializers import TecnologiaSerializer
from django.core import serializers
from app.models import tblTecnologia
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

class Tipo_evento(ListCreateAPIView):
    model = tblTipo_evento
    ordering=('-name',)

class Tecnologia(ListCreateAPIView):
    model = tblTecnologia

class Evento (ListCreateAPIView):
    model = tblEvento 

class Reporte(ListCreateAPIView):
    model = tblReporte

class Denuncia(ListCreateAPIView):
    model = tblDenuncia

class Habilidad(ListCreateAPIView):
    model = tblHabilidad

class Asignacion_idioma(ListCreateAPIView):
    model = tblAsignacion_idioma 

class User_profile(ListCreateAPIView):
    model = tblUser_profile

class Galeria(ListCreateAPIView):
    model = tblGaleria

class Asignacion_habilidad(ListCreateAPIView):
    model = tblAsignacion_habilidad

class Proyecto(ListCreateAPIView):
    model = tblProyecto

class Usuario(ListCreateAPIView):
    model = User
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

def home(request):
    template = "inicio.html"
    return render(request, template)

def perfil(request, slug):
    template = "perfil.html"
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
    persona = User.objects.get(username = kwargs['nombre'])
    habilidad = tblHabilidad.objects.filter(usuario = persona).order_by('dominio')
    tecno = tblTecnologia.objects.filter(nombre=habilidad.tecnologia.nombre)
    serializer = TecnologiaSerializer(tecno, many=True)
    return HttpResponse(serializer.data, mimetype='application/json')

@api_view(['GET', 'POST'])
def tecnologias(request):
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

@api_view(['PUT', 'DELETE'])
def tecnologiaMetodos(request, pk): 
    """
    metodos borrar y modificar
    """          
    try:
        tecno = tblTecnologia.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = TecnologiaSerializer(tecno, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tecno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)