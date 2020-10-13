from django.db import models

# Create your models here.

class carga(models.Model):
	nombre=models.CharField(max_length=50)
	bibliografia=models.CharField(max_length=400)
	foto=models.ImageField(upload_to='carga')
	fecha_nacimiento=models.DateTimeField()
	fecha_defuncion=models.DateTimeField()
	class Meta:
		verbose_name='carga'
		verbose_name_plural='cargas'

	def __str__(self):
		return self.nombre