from distutils.command.upload import upload
from hashlib import blake2b
from mailbox import NoSuchMailboxError
from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.
class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name="categoria_Prod"
        verbose_name_plural="categoriasProd"


    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="tienda",null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
















