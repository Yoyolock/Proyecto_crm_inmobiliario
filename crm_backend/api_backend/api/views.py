from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import pagination
from elasticsearch import Elasticsearch
from api_backend.models import Cliente, Propiedad, AgenteInmobiliario, Administrador, Tarea, Reunion, Venta, Alquiler, Asignacion, TareaAsignada, ReunionProgramada
from api_backend.api.serializers import  ClienteSerializer, PropiedadSerializer, AgenteInmobiliarioSerializer, AdministradorSerializer, TareaSerializer, ReunionSerializer, VentaSerializer, AlquilerSerializer, AsignacionSerializer, TareaAsignadaSerializer, ReunionProgramadaSerializer

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10
    page_query_param = 'p'

class ClienteApiViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    pagination_class = CustomPagination

class PropiedadApiViewSet(ModelViewSet):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadSerializer
    pagination_class = CustomPagination

class AgenteInmobiliarioApiViewSet(ModelViewSet):
    queryset = AgenteInmobiliario.objects.all()
    serializer_class = AgenteInmobiliarioSerializer
    pagination_class = CustomPagination

class AdministradorApiViewSet(ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer
    pagination_class = CustomPagination

class TareaApiViewSet(ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    pagination_class = CustomPagination

class ReunionApiViewSet(ModelViewSet):
    queryset = Reunion.objects.all()
    serializer_class = ReunionSerializer
    pagination_class = CustomPagination

class VentaApiViewSet(ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    pagination_class = CustomPagination

class AlquilerApiViewSet(ModelViewSet):
    queryset = Alquiler.objects.all()
    serializer_class = AlquilerSerializer
    pagination_class = CustomPagination

class AsignacionApiViewSet(ModelViewSet):
    queryset = Asignacion.objects.all()
    serializer_class = AsignacionSerializer
    pagination_class = CustomPagination

class TareaAsignadaApiViewSet(ModelViewSet):
    queryset = TareaAsignada.objects.all()
    serializer_class = TareaAsignadaSerializer
    pagination_class = CustomPagination

class ReunionProgramadaApiViewSet(ModelViewSet):
    queryset = ReunionProgramada.objects.all()
    serializer_class = ReunionProgramadaSerializer
    pagination_class = CustomPagination