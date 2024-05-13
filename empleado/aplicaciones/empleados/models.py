from django.db import models
from aplicaciones.departamento.models import Departamento

# Create your models here.


class Empleado(models.Model):

    JOB_CHOICES = (
        ('0', 'contandor'),
        ('1', 'administrador'),
        ('2', 'economista'),
        ('3', 'otro'),
    )

    first_name = models.CharField('Nombre',max_length=20,null=False)
    last_name = models.CharField('Apellidos', max_length=30, null=False)
    job = models.CharField('Trabajo', max_length=1,choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, on_update=models.CASCADE)
    #image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)


    