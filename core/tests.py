from django.test import TestCase

from .forms import crearProyectoForm, crearSeccionForm, crearTareaForm
from .models import Proyecto, Seccion, Tarea
from rest_framework import status
from rest_framework.test import APITestCase
from .views import *

class proyectoTestCase(TestCase):
	def test_crear_proyecto(self):
		p = Proyecto(nombre="test", desc="descripción de test", url="http://url.com")
		p.save()
		self.assertEqual(p.nombre,"test")
		print("Creado proyecto con éxito")
		
	def test_formulario_proyecto(self):
		datos = { "nombre" : "test", "desc" : "descripción de test", "url" : "http://url.com" }
		form = crearProyectoForm(data=datos)
		self.assertTrue(form.is_valid())
		print("Formulario para crear proyecto correcto")
		
class seccionTestCase(TestCase):
	def test_crear_seccion(self):
		p = Proyecto(nombre="test", desc="descripción de test", url="http://url.com")
		p.save()
		s = Seccion(nombre="stest", desc="descripción de stest", proyecto=p)
		s.save()
		self.assertEqual(s.nombre,"stest")
		print("Creada sección con éxito")
		
	def test_formulario_seccion(self):
		p = Proyecto(nombre="test", desc="descripción de test", url="http://url.com")
		p.save()
		datos = { "nombre" : "stest", "desc" : "descripcion de stest", "proyecto" : p.id }
		form = crearSeccionForm(data=datos)
		self.assertTrue(form.is_valid())
		print("Formulario para crear sección correcto")
		
class tareaTestCase(TestCase):
	def test_crear_tarea(self):
		p = Proyecto(nombre="test", desc="descripción de test", url="http://url.com")
		p.save()
		s = Seccion(nombre="stest", desc="descripción de stest", proyecto=p)
		s.save()
		t = Tarea(nombre="ttest", desc="descripción de ttest", estado="Pendiente", seccion=s)
		t.save()
		self.assertEqual(t.nombre,"ttest")
		print("Creada tarea con éxito")
		
	def test_formulario_tarea(self):
		p = Proyecto(nombre="test", desc="descripción de test", url="http://url.com")
		p.save()
		s = Seccion(nombre="stest", desc="descripción de stest", proyecto=p)
		s.save()
		datos = { "nombre" : "ttest", "desc" : "descripcion de ttest", "estado" : "Pendiente", "seccion" : s.id }
		form = crearTareaForm(data=datos)
		self.assertTrue(form.is_valid())
		print("Formulario para crear tarea correcto")


class ProyectoRESTTests(APITestCase):
	def test_crear_proyecto(self):
		data = { "nombre" : "test", "desc" : "desc test", "url" : "http://test.test" }
		response = self.client.post("/proyectos/", data, format="json")
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Proyecto.objects.get().nombre, "test")
		print("Creado proyecto correctamente con interfaz REST")
		
	def test_mostrar_proyectos(self):
		pro1 = Proyecto(nombre="test", desc="desc test", url="http://test.test")
		pro1.save()
		pro2 = Proyecto(nombre="test2", desc="desc test2", url="http://test2.test2")
		pro2.save()
		response = self.client.get("/proyectos/")
		self.assertEqual(response.content, b'[{"nombre":"test","desc":"desc test","url":"http://test.test"},{"nombre":"test2","desc":"desc test2","url":"http://test2.test2"}]')
		print("Listado de proyectos realizado con éxito mediante interfaz REST")
		
class SeccionRESTTest(APITestCase):
	def test_mostrar_secciones(self):
		p = Proyecto(nombre="test", desc="desc test", url="http://test.test")
		p.save()
		sec1 = Seccion(nombre="seccion test", desc="desc seccion", proyecto=p)
		sec1.save()
		sec2 = Seccion(nombre="seccion2 test", desc="desc seccion2", proyecto=p)
		sec2.save()
		response = self.client.get("/proyecto/1/")
		self.assertEqual(response.content, b'[{"nombre":"seccion test","desc":"desc seccion","proyecto":1},{"nombre":"seccion2 test","desc":"desc seccion2","proyecto":1}]')
		print("Listado de sección de un proyecto exitoso con interfaz REST")

