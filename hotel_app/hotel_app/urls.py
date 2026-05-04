"""
URL configuration for hotel_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core.views import index_estatico, registro, reserva, reserva_lista, home_cliente, metodo_pago, detalle_habitacion, retroalimentacion_cliente, perfil_cliente, home_admin, iniciar_sesion


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index_estatico, name="index"),
    path("registro/", registro, name="registro"),
    path("reserva/", reserva, name="reserva"),
    path("reserva_lista/", reserva_lista, name="reserva_lista"),
    path("home_cliente/", home_cliente, name="home_cliente"),
    path("metodo_pago/", metodo_pago, name="metodo_pago"),
    path("detalle_habitacion/", detalle_habitacion, name="detalle_habitacion"),
    path("retroalimentacion_cliente/", retroalimentacion_cliente, name="retroalimentacion_cliente" ),
    path("perfil_cliente/", perfil_cliente, name="perfil_cliente"),
    path("home_admin/", home_admin, name="home_admin"),
    path("login/", iniciar_sesion, name="login"),
]