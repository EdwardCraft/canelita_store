from django.db import models

# Create your models here.


class TipoProducto(models.Model):
    Tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.Tipo


class Producto(models.Model):
    No_Producto = models.IntegerField()
    Nom_Producto = models.CharField(max_length=100)
    Precio = models.FloatField()
    Unidades = models.IntegerField()
    Tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    Caracteristicas = models.CharField(max_length=200, blank=True, null=True)
    Imagen = models.ImageField(upload_to='productos/', blank=True)

    def __str__(self):
        return self.Nom_Producto


class Distribuidor(models.Model):
    No_Distribuidor = models.IntegerField()
    Nom_Distribuidor = models.CharField(max_length=100)
    Descripcion = models.CharField(max_length=200)
    Imagen_Dis = models.ImageField(upload_to='distribuidores/', blank=True)

    def __str__(self):
        return self.Nom_Distribuidor


class Venta(models.Model):
    No_Venta = models.IntegerField()
    Nom_Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Precio = models.FloatField()
    Unidades = models.IntegerField()
    Nom_Distribuidor = models.ForeignKey(Distribuidor, on_delete=models.CASCADE)
    Total = models.FloatField()
    Fecha_Ven = models.DateField()

    def __str__(self):
        return "%s" % self.No_Venta


class Registro_Venta(models.Model):
    No_Venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    Nom_Producto = models.CharField(max_length=100)
    Unidades = models.IntegerField()
    Fecha_Reg = models.DateField()
    Total = models.IntegerField()


class Estado(models.Model):
    Estado = models.CharField(max_length=50)

    def __str__(self):
        return self.Estado


class Devolución(models.Model):
    No_Venta = models.ForeignKey(Venta, on_delete=models.CASCADE, null=True)
    Nom_Producto = models.CharField(max_length=100)
    Causa = models.CharField(max_length=200)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    Fecha_Dev = models.DateField()


class Colaboradores(models.Model):
    No_Colaborador = models.IntegerField()
    Nom_Colaborador = models.CharField(max_length=70)
    Rol = models.CharField(max_length=50)
    Carrera = models.CharField(max_length=50)
    Imagen_Col = models.ImageField(upload_to='colaboradores/', blank=True)