from django.shortcuts import render
from django.http import HttpResponse
from usuarioCanelita.models import Usuario
def vista_sesion(request):
    return render(request, "sesion.html")

def vista_registroExitoso(request):
    return render(request, "registroExitoso.html")

def vista_reigstro(request):
    name = ""
    user_name = ""
    password = ""
    if request.method == "POST" and  ("name" in request.POST) and ("user_name" in request.POST) and  ("pass" in request.POST):
        name = request.POST["name"]
        user_name = request.POST["user_name"]
        password = request.POST["pass"]
        c = Usuario(Nombre=name, Usuario=user_name, Contraseña=password)
        c.save()
        return render(request, "registroExitoso.html")
    else:
        print(request.POST)
    return render(request, 'registro.html')