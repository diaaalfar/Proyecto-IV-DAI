from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Proyecto, Seccion, Tarea
from .serializers import ProyectoSerializer, SeccionSerializer, TareaSerializer
from django.shortcuts import render

class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)
		
def index(request):
	return render(request, 'scrumpy/index.html')


@csrf_exempt
def lista_proyectos(request):
	"""
	Lista los proyectos, o crea uno
	"""
	if request.method == 'GET':
		proyectos = Proyecto.objects.all()
		serializer = ProyectoSerializer(proyectos, many=True)
		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ProyectoSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def proyecto(request, pk):
	"""
	Lista las secciones que tiene un proyecto o también puedes borrar un proyecto
	"""
	try:
		proyecto = Proyecto.objects.get(pk=pk)
	except Proyecto.DoesNotExist:
		return JSONResponse(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		secciones = proyecto.seccion_set.all()
		serializer = SeccionSerializer(secciones, many=True)
		return JSONResponse(serializer.data)

	elif request.method == 'DELETE':
		proyecto.delete()
		return JSONResponse(status=status.HTTP_204_NO_CONTENT)
		
