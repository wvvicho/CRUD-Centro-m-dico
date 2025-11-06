from django import forms
from .models import Especialidad, Medico, Paciente, Cita

class FormEspecialidad (forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre de la especialidad'
        }
