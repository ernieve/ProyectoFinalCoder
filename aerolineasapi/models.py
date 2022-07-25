from django.db import models
from django.conf import settings
from django.forms import IntegerField
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
#Importar el editor de texto enriquecido, luego de haberlo instalado (pip install django-ckeditor)
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.
TIPOS_AVION = (
    ("COMERCIAL", "Comercial"),
    ("SANITARIO", "Sanitario")
)


class Avion(models.Model):
    modelo = models.CharField(max_length=100)
    # capacidad = models.CharField(max_length=50)
    estado = models.BooleanField()
    fabricante = models.CharField(max_length=100)
    anio = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add= True)
#     updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.modelo}"

# class Pasajero(models.Model):
#     persona = models.CharField(max_length=150)
#     documento = models.CharField(max_length=100)
#     fecha_nacimiento = models.DateField()
#     created_at = models.DateTimeField(auto_now_add= True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self) -> str:
#         return f"{self.persona} - {self.documento}"

class Pais(models.Model):
    pais = models.CharField(max_length=150)
    estado = models.BooleanField()
    imagen = models.ImageField(upload_to='paises', null=True)
    slug = models.SlugField(unique= True, max_length=100, blank= True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.pais}"

def pais_pre_save(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.pais)
pre_save.connect(pais_pre_save, sender=Pais)

class Destino(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    destino = models.CharField(max_length=150)
    estado = models.BooleanField()
    imagen = models.ImageField(upload_to='destinos', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.pais.pais} - {self.destino}"

class Vuelo(models.Model):
    avion = models.ForeignKey(Avion, on_delete=models.CASCADE)
    piloto = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    fecha_salida = models.DateField(null=True, blank=True)
    cupos = models.IntegerField()
    estado = models.BooleanField()
    espacios_ocupados = models.SmallIntegerField(null=True, blank=True)
    cupos_disponibles = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.destino.destino}"

def pre_save_vuelo(sender, instance, *args, **kwargs):
    pasajeros = VueloPasajero.objects.filter(vuelo_id=instance.id)
    instance.espacios_ocupados = len(pasajeros)
    if instance.espacios_ocupados >= int(instance.cupos):
        instance.cupos_disponibles = False
pre_save.connect(pre_save_vuelo, sender=Vuelo)

# class VueloPasajero(models.Model):
#     vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)
#     pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
class Article(models.Model):
    corta_desc=models.CharField(max_length=150,verbose_name='Descripcion Corta')
    content=RichTextField(verbose_name='Contenido')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='Creado el')
    updated_at=models.DateTimeField(auto_now=True,verbose_name='Editado el')
    #Aqui creo relacion, osea FK, con el modelo de usuarios. El cascade borrara todos los articulos si es usuario es eliminado, es decir, no habra ER
    #El editable es para evitar que al crear un articulo los usuarios no puedan asignarlos a otros y se relacionen directamente a quien los crea
    user = models.ForeignKey(User, verbose_name='Usuario',on_delete=models.CASCADE, editable=False)
    
    class Meta:
        verbose_name='Articulo'
        verbose_name_plural='Articulos'
        ordering=['-created_at']
        
    def __str__(self):
        return self.corta_desc

class VueloPasajero(models.Model):
    vuelo_id = models.CharField(max_length=150,verbose_name='destino')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)