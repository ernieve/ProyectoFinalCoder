# Generated by Django 3.2 on 2022-07-17 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerolineasapi', '0004_pais_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='destino',
            name='fecha_salida',
            field=models.DateField(blank=True, null=True),
        ),
    ]