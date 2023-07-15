from django.db import models

class Cliente(models.Model):
    ID_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=100)

class Propiedad(models.Model):
    ID_propiedad = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    num_habitaciones = models.IntegerField()

class AgenteInmobiliario(models.Model):
    ID_agente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=100)

class Administrador(models.Model):
    ID_admin = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=100)

class Tarea(models.Model):
    ID_tarea = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    fecha_limite = models.DateField()
    estado = models.BooleanField(default=False)

class Reunion(models.Model):
    ID_reunion = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)

class Venta(models.Model):
    ID_venta = models.AutoField(primary_key=True)
    fecha_venta = models.DateField()
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)

class Alquiler(models.Model):
    ID_alquiler = models.AutoField(primary_key=True)
    fecha_alquiler = models.DateField()
    precio_alquiler = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)

class Asignacion(models.Model):
    ID_asignacion = models.AutoField(primary_key=True)
    agente = models.ForeignKey(AgenteInmobiliario, on_delete=models.CASCADE)
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField()

class TareaAsignada(models.Model):
    ID_tarea_asignada = models.AutoField(primary_key=True)
    agente = models.ForeignKey(AgenteInmobiliario, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField()

class ReunionProgramada(models.Model):
    ID_reunion_programada = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    reunion = models.ForeignKey(Reunion, on_delete=models.CASCADE)
    fecha_programacion = models.DateField()