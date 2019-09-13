from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from.models import *

def cargar_inicio (request):
    return render(request, "miapp/inicio.html")

class contactanosCreate(CreateView):
    model = contactanos
    fields = ['nombre','correo','telefono','mensaje']
    template_name = 'miapp/contactanos.html'

class almacenCreate(CreateView):
    model = almacen
    fields = ['usuario','nombreA','ciudad','direccion','telefono','nit','correo']
    template_name = 'miapp/almacen.html'

#class tallerCreate(CreateView):
  #  model = taller
 #   fields = ['usuario','nombre','ciudad','direccion','telefono','nit','correo']
  #  template_name = 'miapp/.html'

class productoSucursalCreate(CreateView):
    model = productoSucursal
    fields = ['descripcion','estado','cantidadDisponible','precioMetro','sucursal','producto','textura']
    template_name = 'miapp/productoSucursal.html'

class productoCreate(CreateView):
    model = producto
    fields = ['nombreTela']
    template_name = 'miapp/producto.html'