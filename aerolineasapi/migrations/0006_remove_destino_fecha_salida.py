# Generated by Django 3.2 on 2022-07-19 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aerolineasapi', '0005_destino_fecha_salida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destino',
            name='fecha_salida',
        ),
    ]
