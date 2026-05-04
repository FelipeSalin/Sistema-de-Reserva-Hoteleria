from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login_estatico(request):
    return render(request, 'login.html') 

#vista de registro
def registro(request):
    return render(request, 'registro.html') 

#vista de reserva
def reserva(request):
    return render(request, 'reserva.html') 

#vista home-cliente
#def home_cliente(request):
    #return render(request, 'home_cliente.html') 

#vista home-cliente
def metodo_pago(request):
    return render(request, 'metodo_pago.html') 

#vista detalle habitacion
def detalle_habitacion(request):
    return render(request, 'detalle_habitacion.html') 

# creamos autenticación para home_cliente 
def iniciar_sesion(request):
    formulario = AuthenticationForm()
    context = {
        "formulario": formulario
    }

    return render(request, 'autenticacion/home_cliente.html', context)