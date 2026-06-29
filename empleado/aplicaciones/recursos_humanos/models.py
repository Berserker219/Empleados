from django.db import models
from aplicaciones.empleados.models import Empleado

class Vacaciones(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    dias_totales = models.IntegerField(default=20)
    dias_usados = models.IntegerField(default=0)
    fecha_solicitud = models.DateField(auto_now_add=True)
    aprobado = models.BooleanField(default=False)

    @property
    def dias_restantes(self):
        return self.dias_totales - self.dias_usados


class Solicitud(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)  # vacaciones, permiso, certificado
    descripcion = models.TextField(blank=True, null=True)
    fecha_solicitud = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[('pendiente', 'Pendiente'), ('aprobado', 'Aprobado'), ('rechazado', 'Rechazado')],
        default='pendiente'
    )


class Certificado(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)  # constancia laboral, carta recomendación, etc.
    fecha_solicitud = models.DateField(auto_now_add=True)
    entregado = models.BooleanField(default=False)


class Beneficio(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)


class Permiso(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    aprobado = models.BooleanField(default=False)


class Asistencia(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    presente = models.BooleanField(default=True)
    hora_entrada = models.TimeField(null=True, blank=True)
    hora_salida = models.TimeField(null=True, blank=True)
