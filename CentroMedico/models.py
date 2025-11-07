from django.db import models

# Create your models here.
class Especialidad (models.Model):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Medico (models.Model):
    nombre_completo = models.CharField(max_length=70)
    rut = models.CharField(unique=True, max_length=10)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, related_name='medicos')
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"Médico: {self.nombre_completo}, Especialidad: {self.especialidad}"

class Paciente (models.Model):
    nombre_completo = models.CharField(max_length=70)
    rut = models.CharField(unique=True, max_length=10)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    sexo = models.CharField(max_length=1)
    telefono = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.nombre_completo

class Cita (models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas')
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='citas')
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, related_name='citas')
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    observaciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Fecha cita = {self.fecha_cita}, Hora cita = {self.hora_cita}"
