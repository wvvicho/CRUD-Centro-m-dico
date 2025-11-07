from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import FormEspecialidad
from .models import Especialidad

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

class ActualizarEspecialidades(UpdateView):
    pass

class EliminarEspecialidades(DeleteView):
    pass