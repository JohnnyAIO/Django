from django.db import models
from django.urls import reverse
#from __future__ import unicode_literals

# Create your models here.

def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

class Post(models.Model):
	titulo = models.CharField(max_length=150)
	imagen = models.ImageField(upload_to=upload_location, null=True, blank=True, height_field="height_field", width_field="width_field")
	height_field = models.IntegerField(default=0)
	width_field =  models.IntegerField(default=0)
	contenido = models.TextField()
	timesmap = models.DateTimeField(auto_now_add=True,auto_now=False)
	actualizado = models.DateTimeField(auto_now_add=False,auto_now=True)

	def __str__(self): #Python3 __str__
		return self.titulo

	def get_absolute_url(self):
		return reverse("details", kwargs={"id":self.id})

	class Meta:
		ordering = ["-timesmap"]
