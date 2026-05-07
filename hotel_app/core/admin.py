from django.contrib import admin
from .models import Hotel, Habitacion, Cliente, Reserva, MetodoPago, Factura
# Register your models here.

admin.site.register(Hotel)
admin.site.register(Habitacion)
admin.site.register(Cliente)
admin.site.register(Reserva)
admin.site.register(MetodoPago)
admin.site.register(Factura)