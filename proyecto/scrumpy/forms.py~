from django import forms
from .models import Proyecto, Seccion, Tarea

class crearProyectoForm(forms.ModelForm):
	class Meta:
		model = Proyecto
		fields = ( 'nombre', 'desc', 'url')
		
class crearSeccionForm(forms.ModelForm):
	class Meta:
		model = Seccion
		fields = ( 'nombre', 'desc', 'proyecto' )

class crearTareaForm(forms.ModelForm):
	class Meta:
		model = Tarea
		fields = ( 'nombre', 'desc', 'estado', 'seccion' )

