from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cliente,Propiedad,Administrador,AgenteInmobiliario,Tarea,Reunion,Venta,Alquiler,Asignacion,TareaAsignada,ReunionProgramada

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Propiedad)
admin.site.register(AgenteInmobiliario)
admin.site.register(Administrador)
admin.site.register(Tarea)
admin.site.register(Reunion)
admin.site.register(Venta)
admin.site.register(Alquiler)
admin.site.register(Asignacion)
admin.site.register(TareaAsignada)
admin.site.register(ReunionProgramada)