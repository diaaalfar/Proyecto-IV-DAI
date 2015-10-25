from django.db import models

class Proyecto(models.Model):
	nombre = models.CharField(max_length=100)
	desc = models.TextField()
	url = models.URLField(max_length=300)
	
	def __str__(self):
		return self.nombre
	
class Seccion(models.Model):
	nombre = models.CharField(max_length=100)
	desc = models.TextField()
	proyecto = models.ForeignKey(Proyecto)
	
	def __str__(self):
		return self.nombre

class Tarea(models.Model):
	nombre = models.CharField(max_length=100)
	posibles_estados = ( ('Pendiente', 'Pendiente'),
		('En progreso', 'En progreso'),
		('En pruebas', 'En pruebas'),
		('Completado', 'Completado'),
		)
	desc = models.TextField()
	estado = models.CharField(max_length=12, choices=posibles_estados, default='Pendiente')
	seccion = models.ForeignKey(Seccion)
	
	def __str__(self):
		return self.nombre
