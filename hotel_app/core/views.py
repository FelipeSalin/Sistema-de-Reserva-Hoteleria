from django.shortcuts import render

# Create your views here.
def login_estatico(request):
    return render(request, 'login.html') 

#vista de registro
def registro(request):
    return render(request, 'registro.html') 

#vista de reserva
def reserva(request):
    return render(request, 'reserva.html') 