from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import FormEspecialidad, FormMedico, FormPaciente, FormCita
from .models import Especialidad, Medico, Paciente, Cita

# Create your views here.
def index(req):
    return render(req, 'base.html')

#CRUD de Especialidades

class ListarEspecialidades(ListView):
    model = Especialidad
    template_name = 'listar_especialidades.html'
    context_object_name = 'especialidades'

class CrearEspecialidades(CreateView):
    model = Especialidad
    form_class = FormEspecialidad
    template_name = 'form_especialidades.html'
    success_url = reverse_lazy('listar_especialidades')

    def form_valid(self, form):
        messages.success(self.request, "Especialidad ingresada correctamente!")
        return super().form_valid(form)

class ActualizarEspecialidades(UpdateView):
    model = Especialidad
    form_class = FormEspecialidad
    template_name = 'form_especialidades.html'
    success_url = reverse_lazy('listar_especialidades')

    def form_valid(self, form):
        messages.success(self.request, "Especialidad actualizada con éxito!")
        return super().form_valid(form)

class EliminarEspecialidades(DeleteView):
    model = Especialidad
    template_name = 'confirmar_eliminar.html'
    success_url = reverse_lazy('listar_especialidades')
    
    def form_valid(self, form):
        messages.success(self.request, "Especialidad eliminada con éxito!")
        return super().form_valid(form)
    


#CRUD de Médicos

class ListarMedicos(ListView):
    model = Medico
    template_name = 'listar_medicos.html'
    context_object_name = 'medicos'

class CrearMedicos(CreateView):
    model = Medico
    form_class = FormMedico
    template_name = 'form_medicos.html'
    success_url = reverse_lazy('listar_medicos')

    def form_valid(self, form):
        messages.success(self.request, "Médico ingresado con éxito!")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        contexto =  super().get_context_data(**kwargs)
        contexto["hay_especialidad"] = Especialidad.objects.exists()

        return contexto
    
class EliminarMedicos(DeleteView):
    model = Medico
    template_name = 'confirmar_eliminar.html'
    success_url = reverse_lazy('listar_medicos')

    def form_valid(self, form):
        messages.success(self.request, "Médico eliminado con éxito!")
        return super().form_valid(form)

class ActualizarMedicos(UpdateView):
    model = Medico
    form_class = FormMedico
    template_name = 'form_medicos.html'
    success_url = reverse_lazy('listar_medicos')

    def form_valid(self, form):
        messages.success(self.request, "Médico actualizado con éxito!")
        return super().form_valid(form)
    

#CRUD de Paciente

class ListarPacientes (ListView):
    model = Paciente
    template_name = 'listar_pacientes.html'
    context_object_name = 'pacientes'

class CrearPacientes (CreateView):
    model = Paciente
    form_class = FormPaciente
    template_name = 'form_pacientes.html'
    success_url = reverse_lazy('listar_pacientes')

    def form_valid(self, form):
        messages.success(self.request, "Paciente ingresado con éxito!")
        return super().form_valid(form)
    
class EliminarPacientes (DeleteView):
    model = Paciente
    template_name = 'confirmar_eliminar.html'
    success_url = reverse_lazy('listar_pacientes')
    
    def form_valid(self, form):
        messages.success(self.request, "Paciente eliminado con éxito!")
        return super().form_valid(form)
    
class ActualizarPaciente (UpdateView):
    model = Paciente
    form_class = FormPaciente
    template_name = 'form_pacientes.html'
    success_url = reverse_lazy('listar_pacientes')

    def form_valid(self, form):
        messages.success(self.request, "Paciente actualizado con éxito!")
        return super().form_valid(form)
    

#CRUD de Citas

class ListarCitas (ListView):
    model = Cita
    template_name = 'listar_citas.html'
    context_object_name = 'citas'

class CrearCitas (CreateView):
    model = Cita
    form_class = FormCita
    template_name = 'form_citas.html'
    success_url = reverse_lazy('listar_citas')

    def get_context_data(self, **kwargs):
        contexto =  super().get_context_data(**kwargs)
        contexto["hay_paciente"] = Paciente.objects.exists()
        contexto["hay_medico"] = Medico.objects.exists()
        contexto["hay_especialidad"] = Especialidad.objects.exists()

        return contexto
    
    def form_valid(self, form):
        messages.success(self.request, "Cita ingresada con éxito!")
        return super().form_valid(form)