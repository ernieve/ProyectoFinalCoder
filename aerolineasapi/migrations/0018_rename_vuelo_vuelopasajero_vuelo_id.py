# Generated by Django 4.0.6 on 2022-07-25 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aerolineasapi', '0017_delete_pasajero'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vuelopasajero',
            old_name='vuelo',
            new_name='vuelo_id',
        ),
    ]