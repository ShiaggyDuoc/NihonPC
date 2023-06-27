from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(null=False, max_length=50)

    def __str__(self):
        return self.nombre
    
class TipoProducto(models.Model):
    nombre = models.CharField(null=False, max_length=50)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.IntegerField()
    correo = models.EmailField()
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre