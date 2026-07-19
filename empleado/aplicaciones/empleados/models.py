from django.db import models
from aplicaciones.departamento.models import Departamento
from datetime import date

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    def __str__(self):
        return self.habilidad


class Empleado(models.Model):
    # ===== Datos personales =====
    first_name = models.CharField('Nombre', max_length=20, null=False)
    last_name  = models.CharField('Apellidos', max_length=30, null=False)
    full_name = models.CharField('Nombre completo', max_length=120, blank=True, null=False)
    genero = models.CharField(
        'Género',
        max_length=1,
        choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')],
        blank=True
    )
    fecha_nacimiento = models.DateField('Fecha de nacimiento', null=True, blank=True)
    direccion = models.TextField('Dirección', blank=True, null=True)
    telefono = models.CharField('Teléfono', max_length=20, blank=True, null=True)
    correo = models.EmailField('Correo electrónico', blank=True, null=True)
    contacto_emergencia = models.CharField('Contacto de emergencia', max_length=100, blank=True, null=True)
    telefono_emergencia = models.CharField('Teléfono de emergencia', max_length=20, blank=True, null=True)
    avatar = models.ImageField(upload_to='empleado', null=True, blank=True)

    # ===== Datos laborales =====
    job = models.CharField('Trabajo', max_length=50, null=False)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    fecha_contratacion = models.DateField('Fecha de contratación', null=True, blank=True)
    salario = models.DecimalField('Salario', max_digits=10, decimal_places=2, null=True, blank=True)
    activo = models.BooleanField('Activo', default=True)
    habilidades = models.ManyToManyField(Habilidades, blank=True)

    # ===== Documentación =====
    identificacion = models.FileField(upload_to='documentos/identificaciones', blank=True, null=True)
    contrato = models.FileField(upload_to='documentos/contratos', blank=True, null=True)
    comprobante_domicilio = models.FileField(upload_to='documentos/comprobantes', blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} ({self.job})"

    # ===== Métodos de negocio =====
    @property
    def antiguedad(self):
        if self.fecha_contratacion:
            return (date.today() - self.fecha_contratacion).days // 365
        return 0

    @property
    def cumpleaños(self):
        if not self.fecha_nacimiento:
            return None

        hoy = date.today()
        dia, mes, año = self.fecha_nacimiento.day, self.fecha_nacimiento.month, self.fecha_nacimiento.year
        cumple = date(hoy.year, mes, dia)

        if cumple < hoy:
            cumple = date(hoy.year + 1, mes, dia)

        edad = hoy.year - año
        if (hoy.month, hoy.day) < (mes, dia):
            edad -= 1

        dias_faltan = (cumple - hoy).days

        return {
            "edad": edad,
            "dias_faltan": dias_faltan,
            "proximo_cumple": cumple
        }
