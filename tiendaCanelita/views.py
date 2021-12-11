from django.shortcuts import render
from django.shortcuts import render

def vista_home(request):
    return render(request, "home.html")

def vista_prodctos(request):
    return render(request, 'productos.html')

def vista_distribuidores(request):
    return render(request, 'distribuidores.html')

def vista_colaboradores(request):
    return render(request, 'colaboradores.html')

#Por el momento es esta ejecutando la pagina de error como view para test
def error_404(request):
    return render(request, '404.html')
