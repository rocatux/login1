from django.db import models

# Create your models here.
class ClienteModel (models.Model):
	nombre = models.CharField(max_length=50)
	dpi = models.CharField(max_length=20)


class IngresarProductoModel (models.Model):
	nombre = models.CharField(max_length=70)
	descripcion = models.TextField(max_length=200)
	precio = models.FloatField()
	cantidad = models.IntegerField()