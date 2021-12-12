import datetime

from django.shortcuts import render
from django.shortcuts import render
from tiendaCanelita.models import *
import random
from django.contrib.auth.decorators import login_required



def vista_home(request):
    return render(request, "home.html")


@login_required
def vista_prodctos(request):
    producto = Producto.objects.all()
    return render(request, 'productos.html', {"producto": producto})

@login_required
def vista_distribuidores(request):
    distribuidor = Distribuidor.objects.all()
    return render(request, 'distribuidores.html', {"distribuidor": distribuidor})

@login_required
def vista_colaboradores(request):
    colaborador = Colaboradores.objects.all()
    return render(request, 'colaboradores.html', {"colaborador": colaborador})

#Por el momento es esta ejecutando la pagina de error como view para test
def error_404(request):
    return render(request, '404.html')

def view_compra(request, id):
    producto = Producto.objects.get(id=id)
    venta = Venta.objects.all()
    distribuidor = Distribuidor.objects.all()
    return render(request, "compra.html", {'producto': producto, 'venta': venta, "distribuidor": distribuidor})

def view_registroVenta(request, id):
    producto = Producto.objects.get(id=id)
    distribuidores = request.GET["distribuidor"]
    distribuidores_tipo = ""
    unidades = request.GET["unidades"]
    total = producto.Precio * float(unidades)

    if distribuidores == "1":
        distribuidores_tipo = "DHL"
    if distribuidores == "2":
        distribuidores_tipo = "FedEx"
    if distribuidores == "3":
        distribuidores_tipo = "UPS"

    distribuidor = Distribuidor.objects.get(Nom_Distribuidor=distribuidores_tipo)
    producto = Producto.objects.get(id=id)

    venta = Venta(
        No_Venta=random.randint(0, 100000),
        Precio=producto.Precio,
        Unidades=float(unidades),
        Total=total,
        Fecha_Ven=datetime.datetime.now(),
        Nom_Distribuidor=distribuidor,
        Nom_Producto=producto,
    )
    print("venta Nom_Distribuidor: ",venta.Nom_Distribuidor)
    venta.save()

    no_venta = Venta.objects.get(No_Venta=venta.No_Venta)
    print(no_venta.No_Venta)
    registro = Registro_Venta(
        No_Venta= no_venta,
        Nom_Producto= producto.Nom_Producto,
        Unidades= venta.Unidades,
        Fecha_Reg= venta.Fecha_Ven,
        Total= venta.Total
    )
    print("registro No_Venta: ", registro.No_Venta)
    registro.save()

    u = producto.Unidades - venta.Unidades
    producto.Unidades = u
    print("unidades finales: ", producto.Unidades, "Venta unidades: ", venta.Unidades)
    producto.save()

    return render(request, "registroVenta.html",{'registro':registro})