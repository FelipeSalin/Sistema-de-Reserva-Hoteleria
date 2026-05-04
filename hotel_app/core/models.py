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
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo_electronico = models.CharField(max_length=30)
    telefono = models.CharField(max_length=12)
    
    def __str__(self):
        return self.nombre
 
 
class Reserva(models.Model):
    cliente =models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    habitacion = models.ForeignKey(Habitacion,on_delete=models.DO_NOTHING)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    cantidad_personas = models.DecimalField(max_digits=2, decimal_places=0) 

    def __str__(self):
        return str(self.id)
 
    
class MetodoPago(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)    

    def __str__(self):
        return self.nombre


class Factura(models.Model):
    descripcion = models.CharField(max_length=50)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.DO_NOTHING)
    monto_total = models.DecimalField(max_digits=8,decimal_places=0)

    def __str__(self):
        return self.descripcion
 
class Transaccion(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.DO_NOTHING)
    fecha_pago = models.DateField()    
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id)