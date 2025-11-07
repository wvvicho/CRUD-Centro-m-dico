from django import forms
from .models import Especialidad, Medico, Paciente, Cita

class FormEspecialidad (forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control border-black w-60'}),
        }
