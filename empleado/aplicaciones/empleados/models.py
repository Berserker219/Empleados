from django.db import models
from aplicaciones.departamento.models import Departamento
from ckeditor.fields import RichTextField
from datetime import date
# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField('habilidad', max_length=50)

    def __str__(self):
        return self.habilidad
    

class Empleado(models.Model):

    first_name = models.CharField('Nombre',max_length=20,null=False)
    last_name  = models.CharField('Apellidos', max_length=30, null=False)
    full_name = models.CharField('Nombre Completos', max_length=120, blank = True, null=False)
    job = models.CharField('Trabajo', max_length=50, null=False)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado',null=True, height_field=None, width_field=None, max_length=None)
    habilidades = models.ManyToManyField(Habilidades)
    fecha_contratacion = models.DateField('Fecha de contratación', null=True, blank=True)
    genero = models.CharField('Género', max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], blank=True)
    salario = models.DecimalField('Salario', max_digits=10, decimal_places=2, null=True, blank=True)
    

    def __str__(self):
        return  self.first_name
    
    # Método para calcular antigüedad
    @property
    def antiguedad(self):
        if self.fecha_contratacion:
            return (date.today() - self.fecha_contratacion).days // 365
        return 0
