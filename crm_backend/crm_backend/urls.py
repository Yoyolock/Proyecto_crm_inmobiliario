from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path
from api_backend.api.router import *
# from api_backend.views import ClienteList, ClienteDetail, PropiedadList, PropiedadDetail, AgenteInmobiliarioList, AgenteInmobiliarioDetail, AdministradorList, AdministradorDetail, TareaList, TareaDetail, ReunionList, ReunionDetail, VentaList, VentaDetail, AlquilerList, AlquilerDetail, AsignacionList, AsignacionDetail, TareaAsignadaList, TareaAsignadaDetail, ReunionProgramadaList, ReunionProgramadaDetail

schema_view = get_schema_view(
     openapi.Info(
         title='Swagger Backend',
         default_version='v2',
         description="Sistema CRM Inmobiliario",
         terms_of_service="https://inmobiliaria-montana.com/politicas-y-practicas",
         contact=openapi.Contact(email="contact@snippets.com"),
         license=openapi.License(name="BSD License"),
     ),
     public=True,
     permission_classes=[permissions.AllowAny],
 )

urlpatterns = [
    #Swagger
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # #Djoser auth urls
    # re_path(r'^auth/', include('djoser.urls')),
    # # djoser auth jwt urls
    # re_path(r'^auth/', include('djoser.urls.jwt')),
    # # Login GUI DRF
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #APP CRM
    path('admin/', admin.site.urls),
    path('cliente/', include(router_api_backend_cli.urls)),
    path('propiedad/', include(router_api_backend_prop.urls)),
    path('agenteInmobiliario/', include(router_api_backend_agin.urls)),
    path('Administrador/', include(router_api_backend_admin.urls)),
    path('tarea/', include(router_api_backend_tarea.urls)),
    path('reunion/', include(router_api_backend_reunion.urls)),
    path('venta/', include(router_api_backend_venta.urls)),
    path('alquiler/', include(router_api_backend_alquiler.urls)),
    path('asignacion/', include(router_api_backend_asignacion.urls)),
    path('tareaAsginada/', include(router_api_backend_tareaAsignada.urls)),
    path('reunionProgramada/', include(router_api_backend_reunionProgramada.urls)),
    #Redirige a static
    re_path(r'^static/(?P<path>.*)$', serve),
    
]