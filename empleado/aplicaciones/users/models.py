from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    # Agrega campos personalizados 
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
    


@receiver(post_save, sender=CustomUser)
def enviar_correo_bienvenida(sender, instance, created, **kwargs):
    if created:  # Solo se ejecuta cuando se crea un nuevo usuario
        subject = 'Bienvenido a ABC Blog'
        message = f'Hola {instance.first_name} {instance.last_name},\n\n' \
                  'Usted se ha registrado satisfactoriamente en el blog.\n' \
                  'Es un placer que seas parte de nuestra familia.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]

        send_mail(subject, message, from_email, recipient_list)