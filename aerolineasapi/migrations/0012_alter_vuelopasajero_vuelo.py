# Generated by Django 4.0.6 on 2022-07-25 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerolineasapi', '0011_avion_vuelo_vuelopasajero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vuelopasajero',
            name='vuelo',
            field=models.CharField(max_length=150, verbose_name='Destino'),
        ),
    ]
