from django.shortcuts import render

def vista_home(request):
    return  render(request, "home.html")

#Por el momento es esta ejecutando la pagina de error como view para test
def error_404(request):
    return render(request, '404.html')
