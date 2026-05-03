from django.shortcuts import render

# Create your views here.
def login_estatico(request):
    return render(request, 'login.html')