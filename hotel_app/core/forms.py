from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")
    first_name = forms.CharField(required=False, label="Nombre")
    last_name = forms.CharField(required=False, label="Apellido")
    #fono = forms.CharField(required=True, label="Teléfono")
    #GENERO_CHOICES = [("M", "Masculino"), ("F", "Femenino"), ("O", "Otro"),]
    #genero = forms.ChoiceField(choices=GENERO_CHOICES, required=True, label="Género")
    #password = forms.CharField(required=True, label="Contraseña")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user