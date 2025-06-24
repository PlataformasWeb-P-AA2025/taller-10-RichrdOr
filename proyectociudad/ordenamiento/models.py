from django.db import models

# Create your models here.

class Parroquia(models.Model):

	C_Ubicacion = [
	('norte', 'Norte'),
	('sur', 'Sur'),
	('este', 'Este'),
	('oeste', 'Oeste'),
	]
	Z_Tipo = [
	('urbana', 'Urbana'),
	('rural', 'Rural'),
	]
	nombre = models.CharField(max_length=50)
	ubicacion = models.CharField(max_length=10, choices=C_Ubicacion)
	tipo = models.CharField(max_length=10, choices=Z_Tipo)

	def __str__(self):
		return "%s %s %s" % (self.nombre, self.ubicacion, self.tipo)

class Ciudadela(models.Model):

	nombre = models.CharField(max_length=50)
	num_viviendas = models.IntegerField()
	num_parques = models.IntegerField()
	num_edificiosR = models.IntegerField()
	parroquia = models.ForeignKey(Parroquia,on_delete=models.CASCADE)

	def __str__(self):
		return "%s %d %d %d %s" % (self.nombre,
								self.num_viviendas,
								self.num_parques,
								self.num_edificiosR,
								self.parroquia)

