from django.contrib import admin
from tiendaCanelita.models import *
from usuarioCanelita.models import *


class ProductoAdmin(admin.ModelAdmin):
    list_display = ("No_Producto", "Nom_Producto", "Precio", "Unidades", "Tipo", "Caracteristicas", "Imagen")
    list_display_links = ("Nom_Producto",)
    list_per_page = 10


class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ("No_Colaborador", "Nom_Colaborador", "Rol", "Carrera", "Imagen_Col")
    list_display_links = ("Nom_Colaborador",)
    exclude = ("No_Colaborador",)


class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ("Tipo",)
    list_display_links = ("Tipo",)
    list_per_page = 10


class Registro_VentaAdmon(admin.ModelAdmin):
    list_display = ("No_Venta", "Nom_Producto", "Unidades", "Fecha_Reg", "Total")
    list_display_links = ("Nom_Producto",)
    list_per_page = 10


class VentaAdmin(admin.ModelAdmin):
    list_display = ("No_Venta", "Nom_Producto","Precio","Unidades","Nom_Distribuidor","Total", "Fecha_Ven")
    list_display_links = ("Nom_Producto",)
    list_per_page = 10


class DevolucionAdmin(admin.ModelAdmin):
    list_display = ("No_Venta","Nom_Producto", "Causa", "Estado", "Fecha_Dev")
    list_display_links = ("Nom_Producto",)
    list_per_page = 10


class DistribuidorAmdin(admin.ModelAdmin):
    list_display = ("No_Distribuidor", "Nom_Distribuidor", "Descripcion", "Imagen_Dis")
    list_display_links = ("Nom_Distribuidor",)
    list_per_page = 10


class EstadoAdmin(admin.ModelAdmin):
    list_display = ("Estado",)
    list_display_links = ("Estado",)


# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Registro_Venta, Registro_VentaAdmon)
admin.site.register(Distribuidor, DistribuidorAmdin)
admin.site.register(Devolución, DevolucionAdmin)
admin.site.register(TipoProducto, TipoProductoAdmin)
admin.site.register(Colaboradores, ColaboradorAdmin)
admin.site.register(Estado, EstadoAdmin)