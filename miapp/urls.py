from django.urls import path
from.views import cargar_inicio, contactanosCreate, almacenCreate, productoSucursalCreate, productoCreate

urlpatterns = [
    path('', cargar_inicio, name='inicio'),
    path('contactanos/', contactanosCreate.as_view(), name = 'contactanos'),
    path('almacen/', almacenCreate.as_view(), name = 'almacen'),
    path('productoSucursal/', productoSucursalCreate.as_view(), name = 'productoSucursal'),
    path('producto/', productoCreate.as_view(), name = 'producto'),
    

    ]