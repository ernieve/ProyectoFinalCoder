from django.http import HttpResponse
from django.shortcuts import render,redirect
from aerolineasapi.models import Avion, Destino, Pais, Vuelo
from helpers.utils import *
from django.db.models import Q
from django.contrib.auth.models import User
from datetime import datetime
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User

def index(request):
    comentarios = Article.objects.all()
    avion = Avion.objects.all().order_by('-id')[:3] #Muestra los ultimos 3 aviones cargados
    return render(request,'users/index.html',{'comentarios': comentarios,'avion':avion})

def VistaAviones(request):
    avion = Avion.objects.all()
    return render(request,"aviones/avion.html",{'avion':avion})

def show_avion(request,id):    
    avion = Avion.objects.get(pk=id)
    detail_avion=ShowForms(initial={
        "modelo":avion.modelo,
                "fabricante":avion.fabricante,
                "anio":avion.anio,
                "estado":avion.estado,
                })
    return render(request,"aviones/show_avion.html",{"show_avion":detail_avion,'avion':avion})

@user_passes_test(lambda u:u.is_staff, login_url='inicio_sesion')
def Crear_Avion(request):
    if request.method == "POST":
        formulario = NuevoAvion(request.POST)
        if formulario.is_valid():
            info_avion = formulario.cleaned_data
            aviones = Avion(modelo = info_avion["modelo"],
                            estado = info_avion["estado"],
                            ####
                            fabricante = info_avion["fabricante"],
                            anio = info_avion["anio"])
                            ####
            aviones.save()
            return redirect("aviones")
        else:
            redirect("crear_aviones")
    form_vacio = NuevoAvion()
    return render(request,"aviones/crear_avion.html",{'form':form_vacio})

@user_passes_test(lambda u:u.is_staff, login_url='inicio_sesion')
def Editar_Avion(request,id):
    
    avion = Avion.objects.get(id=id)
    if request.method == "POST":
        
        formulario = NuevoAvion(request.POST)
        
        if formulario.is_valid():
            info_avion = formulario.cleaned_data
            avion.modelo = info_avion["modelo"]
            avion.estado = info_avion["estado"]
            ####
            avion.fabricante = info_avion["fabricante"]
            avion.anio = info_avion["anio"]
            ####
            avion.save()
            return redirect("aviones")
        
    form_editar=NuevoAvion(initial={"modelo":avion.modelo, 
                                    "estado":avion.estado,
                                    "fabricante":avion.fabricante,
                                    "anio":avion.anio})
    return render(request,"aviones/crear_avion.html",{'form':form_editar})

@user_passes_test(lambda u:u.is_staff, login_url='inicio_sesion')
def Eliminar_Avion(request,id):
    avion = Avion.objects.get(id=id)
    avion.delete()
    return redirect("aviones")

# Create your views here.
def VistaPaises(request):
    pais = Pais.objects.all()
    context = {
        "paises": pais
    }
    return render(request, "destinos/paises/paises.html", context)

#@login_required(login_url='inicio_sesion')
@user_passes_test(lambda u:u.is_superuser, login_url='inicio_sesion')
def CrearPais(request):
    if request.method == "POST":
        Pais.objects.create(
            pais = request.POST["pais"],
            estado = request.POST["estado"],
            imagen = request.FILES["imagen"]
        )
        messages.success(request,'Creaste un objeto pais')
        return redirect('VistaPaises')
        # return HttpResponse("Pais creado exitosamente! <a href='/aerolineasapi/paises'>Volver al Panel de Paises</a>")
    return render(request, "destinos/paises/pais_create.html")

#@login_required(login_url='inicio_sesion')
@user_passes_test(lambda u:u.is_staff, login_url='inicio_sesion')
def EditarPais(request, pk):
    pais = Pais.objects.get(pk=pk)
    context = {
        "pais": pais
    }
    if request.method == "POST":
        pais.pais = request.POST["pais"]
        pais.estado = request.POST["estado"]
        if not request.FILES["imagen"] is None:
            pais.imagen = request.FILES["imagen"]
        pais.save()
        return redirect('VistaPaises')
        #return HttpResponse("Se edito el pais correctamente! <a href='/aerolineasapi/paises'>Volver al Panel de Paises</a>")
    return render(request, "destinos/paises/pais_edit.html", context)

#@login_required(login_url='inicio_sesion')
@user_passes_test(lambda u:u.is_superuser, login_url='inicio_sesion')
def EliminarPais(request, pk):
    pais = Pais.objects.get(pk=pk)
    context = {
        "pais": pais
    }
    if request.method == "POST":
        pais.delete()
        return redirect('VistaPaises')
        #return HttpResponse("Pais eliminado correctamente! <a href='/aerolineasapi/paises'>Volver al Panel de Paises</a>")
    return render(request, "destinos/paises/pais_delete.html", context)

def VistaDestinos(request, slug):
    pais = Pais.objects.get(slug=slug)
    destinos = Destino.objects.filter(pais_id = pais.id)
    context = {
        "pais": pais,
        "destinos": destinos
    }
    return render(request, "destinos/destino/destinos.html", context)

#@login_required(login_url='inicio_sesion')
@user_passes_test(lambda u:u.is_staff, login_url='inicio_sesion')
def CrearDestinos(request, slug):
    pais = Pais.objects.get(slug=slug)
    context = {
        "pais": pais
    }
    if request.method == "POST":
        Destino.objects.create(
            pais_id = request.POST["pais"],
            destino = request.POST["destino"],
            estado = request.POST["estado"],
            imagen = request.FILES["imagen"]
        )
        return redirect('VistaDestinos', slug)
        #return HttpResponse(f"Destino creado correctamente! <a href='/aerolineasapi/paises/{pais.slug}'>Volver al Panel de Paises</a>")
    return render(request, "destinos/destino/destino_create.html", context)

#@login_required(login_url='inicio_sesion')
@user_passes_test(lambda u:u.is_staff, login_url='inicio_sesion')
def EditarDestino(request, pk):
    destino = Destino.objects.get(pk=pk)
    context = {
        "destino": destino
    }
    if request.method == "POST":
        destino.destino = request.POST["destino"]
        destino.estado = request.POST["estado"]
        if not request.FILES.get("imagen") is None:
            destino.imagen = request.FILES.get("imagen")
        destino.save()
        return redirect('VistaDestinos', destino.pais.slug)
        #return HttpResponse(f"Destino editado correctamente! <a href='/aerolineasapi/paises/{destino.pais.slug}'>Volver al Panel de Paises</a>")
    return render(request, "destinos/destino/destino_edit.html", context)

#@login_required(login_url='inicio_sesion')
@user_passes_test(lambda u:u.is_superuser, login_url='inicio_sesion')
def EliminarDestino(request, pk):
    destino = Destino.objects.get(pk=pk)
    context = {
        "destino": destino
    }
    if request.method == "POST":
        destino.delete()
        return redirect('VistaDestinos', destino.pais.slug)
        #return HttpResponse(f"Destino editado correctamente! <a href='/aerolineasapi/paises/{destino.pais.slug}'>Volver al Panel de Paises</a>")
    return render(request, "destinos/destino/destino_delete.html", context)

#@login_required(login_url='inicio_sesion')
@user_passes_test(lambda u:u.is_staff, login_url='inicio_sesion')
def CrearVueloDestino(request):
    paises = Pais.objects.filter(estado=True)
    destino = Destino.objects.filter(estado = True)
    context = {
        "paises": paises,
        "destinos": destino
    }
    return render(request, "vuelos/vuelos_destinos.html", context)

@user_passes_test(lambda u:u.is_staff, login_url='inicio_sesion')
#@login_required(login_url='inicio_sesion')
def CrearVuelo(request, pk):
    destino = Destino.objects.get(pk=pk)
    aviones = Avion.objects.filter(estado = True)
    piloto = User.objects.filter(is_staff= True)

    context = {
        "destino": destino,
        "aviones": aviones,
        "pilotos": piloto
    }
    if request.method == "POST":
        fecha = normalize_fecha(request.POST["fecha_salida"])
        Vuelo.objects.create(
            avion_id = request.POST["avion"],
            piloto_id = request.POST["piloto"],
            destino_id = request.POST["destino"],
            fecha_salida = fecha,
            cupos = request.POST["cupos"],
            estado = request.POST["estado"]
        )
        return redirect('CrearVueloDestino')
        #return HttpResponse("Vuelo creado exitosamente! <a href='/aerolineasapi/vuelos/'>Volver al Panel de Vuelos</a>")
    return render(request, "vuelos/vuelo_create.html", context)

def VistaVuelos(request):
    fecha_hoy = datetime.now()
    qry = Q(fecha_salida__range=("1989-01-01", "2030-01-01")) & Q(estado=True)
    vuelos = Vuelo.objects.filter(qry).order_by("fecha_salida")
    context={
        "vuelos": vuelos
    }
    return render(request, "vuelos/vuelos.html", context)

#### USUARIO
def register_page(request):
    
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        register_form=RegisterForm()
        
        if request.method == 'POST':
            
            register_form = RegisterForm(request.POST)
            
            if register_form.is_valid():
                register_form.save()
                
                messages.success(request, 'Te has registrado correctamente')
                return redirect('inicio')
        return render(request,'users/register.html',{'title':'Registro','register_form':register_form})

@login_required(login_url='inicio_sesion')
def update_user(request,id):
    
    user = User.objects.get(id=id)
    
    if request.method == "POST":
        
        update_form = ChangeForm(request.POST)
        if update_form.is_valid():
            info_user = update_form.cleaned_data
            user.email = info_user["email"]
            user.first_name = info_user["first_name"]
            user.last_name = info_user["last_name"]
            user.save()
            messages.success(request,f'Modificaste tus datos, {user.first_name}')
            return redirect('mostrar',id)
    #get
    formulario_vacio = ChangeForm(initial={"email":user.email,
                                "first_name":user.first_name,
                                "last_name":user.last_name,
                                })
    return render(request,"users/update.html",{'update_form':formulario_vacio})

@login_required(login_url='inicio_sesion')
def show_user(request,id):    
    user = User.objects.get(pk=id)
    detail_user=ShowForm(initial={"email":user.email,
                "first_name":user.first_name,
                "last_name":user.last_name,
                })
    return render(request,"users/show_user.html",{"show_user":detail_user})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('VistaPaises')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')      
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('inicio')
            else:
                messages.warning(request,'No te has identificado correctamente') 
        return render(request,'users/login.html',{'title':'Identificate'})

def logout_user(request):
    logout(request)
    return redirect('inicio')

#Sobre nosotros
def sobre_nosotros(request):
    return render(request,"sobrenosotros/sobrenosotros.html")

####ARTICULOS / COMENTARIOS
@login_required(login_url='inicio_sesion')
def crear_articulo(request):
    #POST 
    if request.method=="POST":
        
        formulario = FormArticulo(request.POST)
        
        if formulario.is_valid():
            
            info_articulo = formulario.cleaned_data
            
            articulo = Article(corta_desc = info_articulo["corta_desc"],
                            content = info_articulo["content"],
                            user_id = request.user.id)
            articulo.save()
                        
            return redirect("inicio")
        
        else:
            redirect("inicio")
    else:
        formulario_vacio = FormArticulo()
        return render(request,"users/form_articulo.html",{'form':formulario_vacio})
    
# @user_passes_test(lambda u:u.is_staff, login_url='inicio_sesion')
@login_required(login_url='inicio_sesion')
def ComprarBoleto(request):
    destino = Destino.objects.all()

    context = {
        "destinos": destino,
    }
    if request.method == "POST":
        boleto = VueloPasajero(vuelo_id = request.POST["destino"],user_id_id = request.user.id)
        boleto.save()
        return redirect('boletos',request.user.id)
    return render(request, "vuelos/comprar_boleto.html", context)

def show_boletos(request,id):
    boletos = VueloPasajero.objects.all().filter(user_id_id=id)
    return render(request,"vuelos/boletos.html",{"boletos":boletos})

def eliminarBoleto(request,id):
    boleto = VueloPasajero.objects.get(pk=id)
    boleto.delete()
    return redirect('boletos',request.user.id)
