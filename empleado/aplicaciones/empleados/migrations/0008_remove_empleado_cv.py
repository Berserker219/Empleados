# Generated by Django 4.2 on 2024-06-15 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0007_rename_hoja_vida_empleado_cv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='CV',
        ),
    ]
