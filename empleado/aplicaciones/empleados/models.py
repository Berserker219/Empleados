from django.db import models
from aplicaciones.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField('habilidad', max_length=50)

    def __str__(self):
        return self.habilidad
    

class Empleado(models.Model):

    JOB_CHOICES = (
        ('0', 'contandor'),
        ('1', 'administrador'),
        ('2', 'economista'),
        ('3', 'otro'),
    )

    first_name = models.CharField('Nombre',max_length=20,null=False)
    last_name  = models.CharField('Apellidos', max_length=30, null=False)
    full_name = models.CharField('Nombre Completos', max_length=120, blank = True, null=False)
    job = models.CharField('Trabajo', max_length=1,choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado',null=True, height_field=None, width_field=None, max_length=None)
    habilidades = models.ManyToManyField(Habilidades)

    def __str__(self):
        return  self.first_name