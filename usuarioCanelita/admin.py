from django.contrib import admin
from usuarioCanelita.models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Usuario", "Contraseña")
    list_per_page = 10


# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)