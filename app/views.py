from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactoForm
from .models import Producto
from django.contrib import messages
from django.http import Http404

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

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
    return render(request, 'producto/procesador.html')

def almacenamiento(request):
    return render(request, 'producto/almacenamiento.html')

def gabinete(request):
    return render(request, 'producto/gabinete.html')

def placa(request):
    return render(request, 'producto/placa.html')

def fuente(request):
    return render(request, 'producto/fuente.html')

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