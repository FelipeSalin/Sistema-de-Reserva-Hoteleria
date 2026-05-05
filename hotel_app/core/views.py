from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate, login


# Create your views here.
def index_estatico(request):
    return render(request, 'index.html') 

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
def home_cliente(request):
    return render(request, 'home_cliente.html') 

#vista metodo pago
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
   

# creamos autenticación para login
def iniciar_sesion(request):
    
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get("username")
            contrasena = formulario.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario,password=contrasena) 
            if usuario is None:
                context = {
                    "formulario": formulario,
                    "error": "Usuario o contraseña incorrectas"    
                }
                return render(request, "autenticacion/login.html", context)
            else:
                login(request, usuario)
                return redirect("home_cliente")
        else:
            context = {
                "formulario": formulario    
        }
        return render(request, "autenticacion/login.html", context)
            
    else:    
        formulario = AuthenticationForm()
        context = {
            "formulario": formulario    
    }
    return render(request, "autenticacion/login.html", context)

#vista de métricas
def metricas(request):
    return render(request, 'metricas.html')

#vista de comentarios
def comentarios(request):
    return render(request, 'comentarios.html')

#Logout
def cerrar_sesion(request):
    return redirect("index")