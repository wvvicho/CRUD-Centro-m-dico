from django import forms
from .models import Especialidad, Medico, Paciente, Cita

class FormEspecialidad (forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control border-black w-60'}),
        }

class FormMedico (forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nombre_completo', 'rut', 'especialidad', 'correo', 'telefono']
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class':'form-control border-black w-60'}),
            'rut': forms.TextInput(attrs={'class':'form-control border-black w-60'}),
            'especialidad': forms.Select(attrs={'class':'form-select border-black w-60'}),
            'correo': forms.EmailInput(attrs={'class':'form-control border-black w-60'}),
            'telefono': forms.TextInput(attrs={'class':'form-control border-black w-60'}),
        }

class FormPaciente (forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre_completo', 'rut', 'fecha_nacimiento', 'sexo', 'telefono']
        widgets = {
            'nombre_completo' : forms.TextInput(attrs={'class':'form-control border-black w-60'}), 
            'rut' : forms.TextInput(attrs={'class':'form-control border-black w-60'}), 
            'fecha_nacimiento' : forms.DateInput(attrs={'class':'form-control border-black w-60', 'type':'date'}), 
            'sexo' : forms.Select(attrs={'class':'form-select border-black w-60'}), 
            'telefono' : forms.TextInput(attrs={'class':'form-control border-black w-60'}),
        }
