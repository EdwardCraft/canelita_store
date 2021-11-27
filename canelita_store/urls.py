
from django.contrib import admin
from django.urls import path
import canelita_store.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.vista_home),
    path('404.html/', views.error_404),
]


#handler404 = views.error_404


