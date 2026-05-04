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

#vista de reserva lista
def reserva_lista(request):
    return render(request, 'reserva_lista.html')  

#vista home-cliente
#def home_cliente(request):
    #return render(request, 'home_cliente.html') 

#vista home-cliente
def metodo_pago(request):
    return render(request, 'metodo_pago.html') 

#vista detalle habitacion
def detalle_habitacion(request):
    return render(request, 'detalle_habitacion.html')

#vista de reserva retroalimentación cliente
def retroalimentacion_cliente(request):
    return render(request, 'retroalimentacion_cliente.html')  

#vista de perfil cliente
def perfil_cliente(request):
    return render(request, 'perfil_cliente.html')

#vista de inicio admin
def home_admin(request):
    return render(request, 'home_admin.html')    

# creamos autenticación para home_cliente 
def iniciar_sesion(request):
    formulario = AuthenticationForm()
    context = {
        "formulario": formulario
    }

    return render(request, 'autenticacion/home_cliente.html', context)