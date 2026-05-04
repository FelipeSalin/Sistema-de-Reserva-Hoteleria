from django.db import models

# Create your models here.

class Hotel(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=50)
    catego = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
    
    
class Habitacion(models.Model): 
    TIPO_CHOICES = [('Turista', 'Turista'),('Premium', 'Premium')]
    tipo = models.CharField(max_length=50,choices=TIPO_CHOICES)
    capacidad = models.CharField(max_length=50)    
    precio = models.DecimalField(max_digits=7, decimal_places=0)
    hotel = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.tipo
    
 
    