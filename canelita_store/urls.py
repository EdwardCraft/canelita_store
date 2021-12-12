
from django.contrib import admin
from django.urls import path
import tiendaCanelita.views as views

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import tiendaCanelita.views as views
import usuarioCanelita.views as user_views
from django.contrib.auth import views as auth_views

#urlpatterns = [
 #   path('admin/', admin.site.urls),
  #  path('home/', views.vista_home),
   # path('404/', views.error_404),
    #path('productos/',views.vista_prodctos),
#]

urlpatterns = [
    url(r'^$', views.vista_home, name='home'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^productos/$', views.vista_prodctos, name='productos'),
    url(r'^distribuidores/$', views.vista_distribuidores, name='distribuidores'),
    url(r'^colaboradores/$', views.vista_colaboradores, name='colaboradores'),
    url(r'^registro/$', user_views.vista_reigstro, name='registro'),
    url(r'^sesionExitoso/$', user_views.vista_registroExitoso, name='registroExitoso'),
    url(r'^sesion/$', user_views.vista_sesion, name='sesion'),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#handler404 = views.error_40


