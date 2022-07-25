from django.urls import path
#from .views import (CrearPais, EditarDestino, EditarPais, EliminarDestino, EliminarPais, VistaDestinos, VistaPaises, CrearDestinos, CrearVueloDestino, CrearVuelo, VistaVuelos)
from .views import *
urlpatterns = [
    # PAISES
    path('paises/', VistaPaises,name="VistaPaises"),
    path('paises/create/', CrearPais, name="CrearPais"),
    path('paises/edit/<int:pk>', EditarPais, name="EditarPais"),
    path('paises/delete/<int:pk>', EliminarPais, name="EliminarPais"),
    # DESTINOS
    path('paises/<slug:slug>', VistaDestinos, name="VistaDestinos"),
    path('destinos/<slug:slug>/create', CrearDestinos, name="CrearDestinos"),
    path('destinos/edit/<int:pk>', EditarDestino, name="EditarDestino"),
    path('destinos/delete/<int:pk>', EliminarDestino, name="EliminarDestino"),
    # VUELOS
    path('vuelos/', VistaVuelos,name="VistaVuelos"),
    path('vuelos/create/', CrearVueloDestino, name="CrearVueloDestino"),
    path('vuelos/create/<int:pk>', CrearVuelo, name="CrearVuelo"),
    # USUARIO
    path('registro/',register_page, name='register'),
    path('inicio_sesion/',login_page, name='inicio_sesion'),
    path('cerrar_sesion/',logout_user,name='logout'),
    path('modificar_user/<int:id>',update_user,name='actualizar'),
    path('mostrar_user/<int:id>',show_user,name='mostrar'),
    path('',index,name="inicio"),
    # AVIONES
    path('aviones/', VistaAviones,name="aviones"),
    path('mostrar_avion/<int:id>',show_avion,name='muestra'),
    path('crear_aviones/',Crear_Avion,name="crear_aviones"),
    path('editar_aviones/<int:id>',Editar_Avion,name="editar_aviones"),
    path('eliminar_aviones/<id>',Eliminar_Avion,name="eliminar_aviones"),
    #Comentarios
    path('crear_articulo/',crear_articulo,name="crear_articulo"),
    #Sobre nosotros
    path('about/', sobre_nosotros, name = "about"),
    #Boletos
    path('boletos/<int:id>',show_boletos, name="boletos"),
    path('comprar_boleto/',ComprarBoleto, name="Comprar_boleto"),
    path('eliminar_boleto/<int:id>',eliminarBoleto, name="eliminar_boleto")
    ]
