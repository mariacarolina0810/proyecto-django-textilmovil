
from django.db import models

from django.contrib.auth.models import User

class rol(models.Model):
    rol = models.CharField(max_length=45)

    def __str__(self):
        return self.rol

 
# class usuario(models.Model):
#     nombre = models.CharField("Nombre:",max_length=45)
#     apellido = models.CharField("apellido:",max_length=45)
#     tipoD = models.CharField(max_length=45)
#     numeroD = models.CharField(max_length=45)
#     telefono = models.CharField(max_length=45)
#     direccion = models.CharField(max_length=45)
#     correo = models.CharField(max_length=45)
#     usuario = models.CharField(max_length=45)
#     contrasena = models.CharField(max_length=45)
#     rol = models.ForeignKey('rol', on_delete=models.CASCADE)
    
#     def __str__(self):
#         return "{0}"-"{1}".format(self.nombre, self.numeroD)

class almacen(models.Model):
    #usuario = models.OneToOneField('User', on_delete=models.CASCADE )
    nombreA = models.CharField("Nombre:",max_length=45)
    ciudad = models.CharField("ciudad:",max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    nit = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)

    def __str__(self):
        return self.nit

class sucursal(models.Model):
    nombre = models.CharField("Nombre:",max_length=45)
    ciudad = models.CharField("ciudad:",max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    alamcen = models.ForeignKey('almacen', on_delete=models.CASCADE)
    usuario = models.ForeignKey('User', on_delete=models.CASCADE)

class tipoIdTaller(models.Model):
    tipo = models.CharField(max_length=45)

class taller(models.Model):
    usuario = models.OneToOneField('User', on_delete=models.CASCADE)
    nombre = models.CharField("Nombre:",max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    nit = models.CharField(max_length=45)
    usuario = models.ForeignKey('User', on_delete=models.CASCADE)
    tipoIdTaller = models.ForeignKey('tipoIdTaller', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nit

class clienteIndependiente(models.Model):
    usuario = models.ForeignKey('User', on_delete=models.CASCADE)

class pedido(models.Model):
    fecha = models.DateField("Fecha")
    observaciones = models.CharField(max_length=45)
    estado = models.BooleanField()
    usuario = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha

class detallePedido(models.Model):
     total = models.IntegerField(null=True)
     fecha = models.DateField("Fecha")
     productoSucursal = models.ForeignKey('productoSucursal', on_delete=models.CASCADE)
    
class factura(models.Model):
     cantidad = models.IntegerField(null=True)
     precio = models.IntegerField(null=True)
     estado = models.BooleanField()
     pedido = models.ForeignKey('pedido', on_delete=models.CASCADE)

class producto(models.Model):
    nombreTela =models.DateField(max_length=45)


class ingresoProducto(models.Model):
    fechaingreso =models.DateField("Fecha de ingreso")
    sucursal = models.ForeignKey('sucursal', on_delete=models.CASCADE)

class detalleIngreso(models.Model):
    cantidad  = models.CharField(max_length=45)
    productoSucursal = models.ForeignKey('productoSucursal', on_delete=models.CASCADE)
    ingresoProducto = models.ForeignKey('ingresoProducto', on_delete=models.CASCADE)


class productoSucursal(models.Model):
    descripcion = models.CharField(max_length=45)
    estado = models.BooleanField()
    cantidadDisponible = models.IntegerField(null=True)
    precioMetro = models.IntegerField(null=True)
    sucursal = models.ForeignKey('sucursal', on_delete=models.CASCADE,related_name='+')
    producto = models.ForeignKey('producto', on_delete=models.CASCADE,related_name='+')
    textura = models.ForeignKey('producto', on_delete=models.CASCADE,related_name='+')

class textura(models.Model):
    textura =models.DateField(max_length=45)

class colortelas(models.Model):
    color =models.DateField(max_length=45)

class productoSucursal_has_colortelas(models.Model):
     productoSucursal = models.ForeignKey('productoSucursal', on_delete=models.CASCADE)
     colortelas = models.ForeignKey('colortelas', on_delete=models.CASCADE)
    
class caracteristicastelas(models.Model):
    caracteristicas =models.DateField(max_length=45)

class productoSucursal_has_caracteristicastelas(models.Model):
     productoSucursal = models.ForeignKey('productoSucursal', on_delete=models.CASCADE)
     caracteristicastelas = models.ForeignKey('caracteristicastelas', on_delete=models.CASCADE)

class uso(models.Model):
    uso =models.DateField(max_length=45)

class productoSucursal_has_uso(models.Model):
     productoSucursal = models.ForeignKey('productoSucursal', on_delete=models.CASCADE)
     uso = models.ForeignKey('uso', on_delete=models.CASCADE)

class contactanos (models.Model):
    nombre = models.CharField("Nombre:",max_length=45)
    correo = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    mensaje = models.CharField(max_length=45)






