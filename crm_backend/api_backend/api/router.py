from rest_framework.routers import DefaultRouter
from api_backend.api.views import  ClienteApiViewSet,PropiedadApiViewSet, AgenteInmobiliarioApiViewSet, AdministradorApiViewSet, TareaApiViewSet, ReunionApiViewSet, VentaApiViewSet, AlquilerApiViewSet, AsignacionApiViewSet, TareaAsignadaApiViewSet, ReunionProgramadaApiViewSet

# Cliente
router_api_backend_cli = DefaultRouter()
router_api_backend_cli.register(prefix='', basename='cliente', viewset=ClienteApiViewSet)
# propiedad
router_api_backend_prop = DefaultRouter()
router_api_backend_prop.register(prefix='', basename='propiedad', viewset=PropiedadApiViewSet)
# agenteInmobiliario
router_api_backend_agin = DefaultRouter()
router_api_backend_agin.register(prefix='', basename='agenteInmobiliario', viewset=AgenteInmobiliarioApiViewSet)
# administrador
router_api_backend_admin = DefaultRouter()
router_api_backend_admin.register(prefix='', basename='administrador', viewset=AdministradorApiViewSet)
# tarea
router_api_backend_tarea = DefaultRouter()
router_api_backend_tarea.register(prefix='', basename='tarea', viewset=TareaApiViewSet)
# reunion
router_api_backend_reunion = DefaultRouter()
router_api_backend_reunion.register(prefix='', basename='reunion', viewset=ReunionApiViewSet)
# venta
router_api_backend_venta = DefaultRouter()
router_api_backend_venta.register(prefix='', basename='venta', viewset=VentaApiViewSet)
# alquiler
router_api_backend_alquiler = DefaultRouter()
router_api_backend_alquiler.register(prefix='', basename='alquiler', viewset=AlquilerApiViewSet)
# asignacion
router_api_backend_asignacion = DefaultRouter()
router_api_backend_asignacion.register(prefix='', basename='asignacion', viewset=AsignacionApiViewSet)
# tareaAsignada
router_api_backend_tareaAsignada = DefaultRouter()
router_api_backend_tareaAsignada.register(prefix='', basename='tareaAsignada', viewset=TareaAsignadaApiViewSet)
# reunionProgramada
router_api_backend_reunionProgramada = DefaultRouter()
router_api_backend_reunionProgramada.register(prefix='', basename='reunionProgramada', viewset=ReunionProgramadaApiViewSet)