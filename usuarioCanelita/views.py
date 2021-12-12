from django.shortcuts import render
from django.http import HttpResponse
from usuarioCanelita.models import Usuario
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

def vista_sesion(request):
    user_name = ""
    password = ""
    if request.method == "POST" and ("user_name" in request.POST) and ("pass" in request.POST):
        user_name = request.POST["user_name"]
        password = request.POST["pass"]
        try:
            user = Usuario.empAuth_objects.get(Usuario=user_name, Contraseña=password)
            print(user)
            if user is not None:
                return render(request, "registroExitoso.html", {'msj': user_name})
            else:
                print(user_name,password)
        except Exception as identifier:
            print(identifier)

    return render(request, "sesion.html")


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

        user = User.objects.create_user(user_name, 'test@gmail.com', password)
        # Update fields and then save again
        user.first_name = name
        user.last_name = name
        user.save()

        return render(request, "registroExitoso.html", {'msj': ""})
    else:
        print(request.POST)
    return render(request, 'registro.html')


def vista_registroExitoso(request):
    return render(request, "registroExitoso.html", {'msj': ""})