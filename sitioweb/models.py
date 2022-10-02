from django.utils import timezone
from django.db import models
from django.db.models import F,Sum, FloatField, IntegerField
from django.contrib.auth.models import User


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    created = models.DateTimeField(default= timezone.now)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100,)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to="Productos", max_length=250, null=True, blank=True)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(default= timezone.now)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return f'{self.nombre} -> {self.precio}'

class Pedido(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.id}'
    
    @property
    def total(self):
        return self.lineapedido_set.aggregate(

            total = Sum(F("precio")*F("cantidad"), output_field=IntegerField())

        )["total"]

class LineaPedido(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.cantidad} Unidades de {self.producto.nombre}'
        
