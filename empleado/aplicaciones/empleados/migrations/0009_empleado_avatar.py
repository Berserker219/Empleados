# Generated by Django 4.2 on 2024-06-25 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0008_remove_empleado_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(null=True, upload_to=None),
        ),
    ]