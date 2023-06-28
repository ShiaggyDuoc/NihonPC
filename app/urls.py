from django.urls import path
from .views import index, nosotros, politica, terminos, envios, devoluciones, contacto, teclado, mouse, tarjeta, procesador, almacenamiento, gabinete, placa, fuente,login,registro

urlpatterns = [
    path('', index, name="index"),
    path('nosotros/', nosotros, name="nosotros"),
    path('politica/', politica, name="politica"),
    path('terminos/', terminos, name="terminos"),
    path('envios/', envios, name="envios"),
    path('devoluciones/', devoluciones, name="devoluciones"),
    path('contacto/', contacto, name="contacto"),
    path('teclado/', teclado, name="teclado"),
    path('mouse/', mouse, name="mouse"),
    path('tarjeta/', tarjeta, name="tarjeta"),
    path('procesador/', procesador, name="procesador"),
    path('almacenamiento/', almacenamiento, name="almacenamiento"),
    path('gabinete/', gabinete, name="gabinete"),
    path('placa/', placa, name="placa"),
    path('fuente/', fuente, name="fuente"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
]