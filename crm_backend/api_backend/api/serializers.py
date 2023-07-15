from rest_framework import serializers
from api_backend.models import Cliente, Propiedad, AgenteInmobiliario, Administrador, Tarea, Reunion, Venta, Alquiler, Asignacion, TareaAsignada, ReunionProgramada
from django.contrib.auth import get_user_model
from rest_framework import exceptions
from elasticsearch import Elasticsearch
import requests as rq
import json
from decouple import config

elastic_url = config("URL_ELASTIC")

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def create(self, validated_data):
        # Llamamos al método `create` del serializer padre para crear el cliente
        cliente = super().create(validated_data)

        # Guardar el cliente en Elasticsearch
        elastic_post_endpoint = f'crmindex/_doc'
        post_body = {
            'ID_cliente': cliente.ID_cliente,
            'nombre': cliente.nombre,
            'direccion': cliente.direccion,
            'telefono': cliente.telefono,
            'correo': cliente.correo,
        }
        # 1print('data elastic', file_data['parameters'], file_data['name_document'], file_data['name_folder'])
        elastic_response = rq.post(
            elastic_url+elastic_post_endpoint,
            json=post_body
        )
        print('resp elastic', json.loads(elastic_response.text))
        elastic_id = json.loads(elastic_response.text)['_id']
        print('id elastic', elastic_id)

        return cliente


class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad
        fields = ('__all__')

    def create(self, validated_data):
        # Llamamos al método `create` del serializer padre para crear la propiedad
        propiedad = super().create(validated_data)

        # Guardar el Propiedad en Elasticsearch
        elastic_post_endpoint = f'crmindex/_doc'
        post_body = {
            'ID_cliente': propiedad.ID_propiedad,
            'direccion': propiedad.direccion,
            'tipo': propiedad.tipo,
            'precio': propiedad.precio,
            'num_habitaciones': propiedad.num_habitaciones,
        }
        # 1print('data elastic', file_data['parameters'], file_data['name_document'], file_data['name_folder'])
        elastic_response = rq.post(
            elastic_url+elastic_post_endpoint,
            json=post_body
        )
        print('resp elastic', json.loads(elastic_response.text))
        elastic_id = json.loads(elastic_response.text)['_id']
        print('id elastic', elastic_id)
        
        return propiedad

class AgenteInmobiliarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgenteInmobiliario
        fields = ('__all__')

    def create(self, validated_data):
        # Llamamos al método `create` del serializer padre para crear el agenteInmobiliario
        agenteInmobiliario = super().create(validated_data)

        # Guardar el agenteInmobiliario en Elasticsearch
        elastic_post_endpoint = f'crmindex/_doc'
        post_body = {
            'ID_agente': agenteInmobiliario.ID_agente,
            'nombre': agenteInmobiliario.nombre,
            'direccion': agenteInmobiliario.direccion,
            'telefono': agenteInmobiliario.telefono,
            'correo': agenteInmobiliario.correo,
        }
        # 1print('data elastic', file_data['parameters'], file_data['name_document'], file_data['name_folder'])
        elastic_response = rq.post(
            elastic_url+elastic_post_endpoint,
            json=post_body
        )
        print('resp elastic', json.loads(elastic_response.text))
        elastic_id = json.loads(elastic_response.text)['_id']
        print('id elastic', elastic_id)
        
        return agenteInmobiliario

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = ('__all__')

    def create(self, validated_data):
        # Llamamos al método `create` del serializer padre para crear el administrador
        administrador = super().create(validated_data)

        # Guardar el administrador en Elasticsearch
        elastic_post_endpoint = f'crmindex/_doc'
        post_body = {
            'ID_admin': administrador.ID_admin,
            'nombre': administrador.nombre,
            'direccion': administrador.direccion,
            'telefono': administrador.telefono,
            'correo': administrador.correo,
        }
        # 1print('data elastic', file_data['parameters'], file_data['name_document'], file_data['name_folder'])
        elastic_response = rq.post(
            elastic_url+elastic_post_endpoint,
            json=post_body
        )
        print('resp elastic', json.loads(elastic_response.text))
        elastic_id = json.loads(elastic_response.text)['_id']
        print('id elastic', elastic_id)
        
        return administrador

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ('__all__')

    def create(self, validated_data):
        # Llamamos al método `create` del serializer padre para crear la tarea
        tarea = super().create(validated_data)

        # Guardar la tarea en Elasticsearch
        elastic_post_endpoint = f'crmindex/_doc'
        post_body = {
            'ID_tarea': tarea.ID_tarea,
            'descripcion': tarea.descripcion,
            'fecha_limite': tarea.fecha_limite,
            'estado': tarea.estado,
        }
        # 1print('data elastic', file_data['parameters'], file_data['name_document'], file_data['name_folder'])
        elastic_response = rq.post(
            elastic_url+elastic_post_endpoint,
            json=post_body
        )
        print('resp elastic', json.loads(elastic_response.text))
        elastic_id = json.loads(elastic_response.text)['_id']
        print('id elastic', elastic_id)
        
        return tarea

class ReunionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reunion
        fields = ('__all__')

    def create(self, validated_data):
        # Llamamos al método `create` del serializer padre para crear la reunion
        reunion = super().create(validated_data)

        # Guardar la reunion en Elasticsearch
        elastic_post_endpoint = f'crmindex/_doc'
        post_body = {
            'ID_tarea': reunion.ID_reunion,
            'fecha': reunion.fecha,
            'hora': reunion.hora,
            'lugar': reunion.lugar,
            'descripcion': reunion.descripcion,
        }
        # 1print('data elastic', file_data['parameters'], file_data['name_document'], file_data['name_folder'])
        elastic_response = rq.post(
            elastic_url+elastic_post_endpoint,
            json=post_body
        )
        print('resp elastic', json.loads(elastic_response.text))
        elastic_id = json.loads(elastic_response.text)['_id']
        print('id elastic', elastic_id)
        
        return reunion

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ('__all__')

    def create(self, validated_data):
        # Llamamos al método `create` del serializer padre para crear la venta
        venta = super().create(validated_data)

        # Guardar la venta en Elasticsearch
        elastic_post_endpoint = f'crmindex/_doc'
        post_body = {
            'ID_venta': venta.ID_venta,
            'fecha_venta': venta.fecha_venta,
            'precio_venta': venta.precio_venta,
            'cliente': venta.cliente,
            'propiedad': venta.propiedad,
        }
        # 1print('data elastic', file_data['parameters'], file_data['name_document'], file_data['name_folder'])
        elastic_response = rq.post(
            elastic_url+elastic_post_endpoint,
            json=post_body
        )
        print('resp elastic', json.loads(elastic_response.text))
        elastic_id = json.loads(elastic_response.text)['_id']
        print('id elastic', elastic_id)
        
        return venta

class AlquilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alquiler
        fields = ('__all__')

    def create(self, validated_data):
        # Llamamos al método `create` del serializer padre para crear el alquiler
        alquiler = super().create(validated_data)

        # Guardar el alquiler en Elasticsearch
        elastic_post_endpoint = f'crmindex/_doc'
        post_body = {
            'ID_alquiler': alquiler.ID_alquiler,
            'fecha_alquiler': alquiler.fecha_alquiler,
            'precio_alquiler': alquiler.precio_alquiler,
            'cliente': alquiler.cliente,
            'propiedad': alquiler.propiedad,
        }
        # 1print('data elastic', file_data['parameters'], file_data['name_document'], file_data['name_folder'])
        elastic_response = rq.post(
            elastic_url+elastic_post_endpoint,
            json=post_body
        )
        print('resp elastic', json.loads(elastic_response.text))
        elastic_id = json.loads(elastic_response.text)['_id']
        print('id elastic', elastic_id)
        
        return alquiler

class AsignacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignacion
        fields = ('__all__')

    def create(self, validated_data):
        # Llamamos al método `create` del serializer padre para crear la asignacion
        asignacion = super().create(validated_data)

        # Guardar la asignacion en Elasticsearch
        elastic_post_endpoint = f'crmindex/_doc'
        post_body = {
            'ID_asignacion': asignacion.ID_asignacion,
            'agente': asignacion.agente,
            'propiedad': asignacion.propiedad,
            'fecha_asignacion': asignacion.fecha_asignacion,
        }
        # 1print('data elastic', file_data['parameters'], file_data['name_document'], file_data['name_folder'])
        elastic_response = rq.post(
            elastic_url+elastic_post_endpoint,
            json=post_body
        )
        print('resp elastic', json.loads(elastic_response.text))
        elastic_id = json.loads(elastic_response.text)['_id']
        print('id elastic', elastic_id)
        
        return asignacion

class TareaAsignadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TareaAsignada
        fields = ('__all__')

    def create(self, validated_data):
        # Llamamos al método `create` del serializer padre para crear la tareaAsignada
        tareaAsignada = super().create(validated_data)

        # Guardar la tareaAsignada en Elasticsearch
        elastic_post_endpoint = f'crmindex/_doc'
        post_body = {
            'ID_tarea_asignada': tareaAsignada.ID_tarea_asignada,
            'agente': tareaAsignada.agente,
            'tarea': tareaAsignada.tarea,
            'fecha_asignacion': tareaAsignada.fecha_asignacion,
        }
        # 1print('data elastic', file_data['parameters'], file_data['name_document'], file_data['name_folder'])
        elastic_response = rq.post(
            elastic_url+elastic_post_endpoint,
            json=post_body
        )
        print('resp elastic', json.loads(elastic_response.text))
        elastic_id = json.loads(elastic_response.text)['_id']
        print('id elastic', elastic_id)
        
        return tareaAsignada

class ReunionProgramadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReunionProgramada
        fields = ('__all__')

    def create(self, validated_data):
        # Llamamos al método `create` del serializer padre para crear la reunionProgramada
        reunionProgramada = super().create(validated_data)

        # Guardar la reunionProgramada en Elasticsearch
        elastic_post_endpoint = f'crmindex/_doc'
        post_body = {
            'ID_reunion_programada': reunionProgramada.ID_reunion_programada,
            'cliente': reunionProgramada.cliente,
            'reunion': reunionProgramada.reunion,
            'fecha_programacion': reunionProgramada.fecha_programacion,
        }
        # 1print('data elastic', file_data['parameters'], file_data['name_document'], file_data['name_folder'])
        elastic_response = rq.post(
            elastic_url+elastic_post_endpoint,
            json=post_body
        )
        print('resp elastic', json.loads(elastic_response.text))
        elastic_id = json.loads(elastic_response.text)['_id']
        print('id elastic', elastic_id)
        
        return reunionProgramada



    # def create(self, validated_data):
    #     # Create de doc
    #     doc = super().create(validated_data)
    #     data_4_task = {
    #         'id_doc': int(doc.id),
    #         'name_folder': validated_data.pop('name_folder'),
    #         'name_company': validated_data.pop('name_company'),
    #         'name_document': validated_data.pop('name'),
    #         'parameters': validated_data.pop('parameters'),
    #     }
    #     t_store_docs.delay(data_4_task)
    #     return doc


# class ClienteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cliente
#         fields = '__all__'

#     def create(self, validated_data):
#         # Llamamos al método `create` del serializer padre para crear el cliente
#         cliente = super().create(validated_data)

#         # Guardar el cliente en Elasticsearch
#         es = Elasticsearch()
#         es.index(index='clientes', id=cliente.id, body=cliente.__dict__)

#         return cliente