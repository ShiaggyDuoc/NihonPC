from django.contrib import admin
from .models import Contacto, Producto, Marca, TipoProducto

# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "numero", "correo"]
    search_fields = ["nombre"]

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "marca", "tipo_producto"]
    search_fields = ["nombre"]


admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Marca)
admin.site.register(TipoProducto)
