# Generated by Django 3.2 on 2022-07-17 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerolineasapi', '0003_destino_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='pais',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]