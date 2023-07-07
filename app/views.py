from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactoForm,CustomUserCreationForm, ProductoForm
from .models import Producto
from django.contrib import messages
from django.http import Http404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required, permission_required

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
            usuario = formulario.save()
            user = authenticate(request, username=usuario.username, password=formulario.cleaned_data["password1"])
            if user is not None:
                auth_login(request, user)
                messages.success(request, "Te has registrado correctamente")
                return redirect('index')
        data["form"] = formulario
    
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

@permission_required('app.add_producto')
def agregar(request):
    data = { 
        'form': ProductoForm()
    }

    if request.method== 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, " Modificado Correctamente")
        else:
            data["form"]=formulario
    
    return render(request, 'formularios/agregar.html', data)

@permission_required('app.view_producto')
def listarP(request):

    productos = Producto.objects.all()

    data = {
        'productos' : productos
    }

    return render(request,'formularios/listarP.html', data)

@permission_required('app.change_producto')
def modificar_producto (request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form' : ProductoForm(instance=producto)
    }

    if request.method== 'POST':
        formulario = ProductoForm(data=request.POST,instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, " Modificado Correctamente")
            return redirect(to='listarP')
        else:
            data["form"]=formulario

    return render(request, 'formularios/modificarP.html',data)

@permission_required('app.delete_producto')
def eliminar_producto (request, id):

    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to='listarP')
