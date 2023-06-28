from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactoForm,CustomUserCreationForm
from .models import Producto
from django.contrib import messages
from django.http import Http404
from django.contrib.auth import authenticate, login 

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def login(request):
    return render(request, 'registration/login.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password= formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "te has registrado correctamente")
            return redirect(to="index")
        data["form"]= formulario
    return render(request, 'registration/registro.html', data)

def nosotros(request):
    return render(request, 'app/nosotros.html')

def politica(request):
    return render(request, 'app/politica.html')

def terminos(request):
    return render(request, 'app/terminos.html')

def envios(request):
    return render(request, 'app/envios.html')

def devoluciones(request):
    return render(request, 'app/devoluciones.html')

def teclado(request):
    productos = Producto.objects.all()
    data = { 
        'productos': productos
    }

    return render(request, 'producto/teclado.html', data)

def mouse(request):
    productos = Producto.objects.all()
    data = { 
        'productos': productos
    }

    return render(request, 'producto/mouse.html', data)

def tarjeta(request):
    productos = Producto.objects.all()
    data = { 
        'productos': productos
    }
    return render(request, 'producto/tarjeta.html', data)

def procesador(request):
    productos = Producto.objects.all()
    data = { 
        'productos': productos
    }

    return render(request, 'producto/procesador.html', data)

def almacenamiento(request):
    productos = Producto.objects.all()
    data = { 
        'productos': productos
    }

    return render(request, 'producto/almacenamiento.html', data)

def gabinete(request):
    productos = Producto.objects.all()
    data = { 
        'productos': productos
    }

    return render(request, 'producto/gabinete.html', data)

def placa(request):
    productos = Producto.objects.all()
    data = { 
        'productos': productos
    }

    return render(request, 'producto/placa.html', data)

def fuente(request):
    productos = Producto.objects.all()
    data = { 
        'productos': productos
    }

    return render(request, 'producto/fuente.html', data)

def contacto(request):
    data = { 
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mensaje Enviado")
        else:
            data["form"] = "formulario"
    
    return render(request, 'app/contacto.html', data)