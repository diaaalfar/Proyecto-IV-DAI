from rest_framework import serializers
from .models import Proyecto, Seccion, Tarea

class ProyectoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Proyecto
		fields = ("nombre", "desc", "url",)
		
class SeccionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Seccion
		fields = ("nombre", "desc", "proyecto",)
		
class TareaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Seccion
		fields = ("nombre", "desc", "estado","seccion",)


