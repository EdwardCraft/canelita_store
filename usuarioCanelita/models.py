from django.db import models

# Create your models here.
class Usuario(models.Model):
    Nombre = models.CharField(max_length=100)
    Usuario = models.CharField(max_length=20)
    Contraseña = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre

    empAuth_objects = models.Manager()
