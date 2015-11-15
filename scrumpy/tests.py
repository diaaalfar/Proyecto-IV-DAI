from django.test import TestCase

from .forms import crearProyectoForm, crearSeccionForm, crearTareaForm
from .models import Proyecto, Seccion, Tarea

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
