from django.db import models
from django.utils import timezone

class Area(models.Model):
	descricao = models.CharField(max_length=100)
	cor = models.CharField(max_length=100)
	status = models.BooleanField()

	def ativar(self):
		self.status = True
		self.save()
	def desativar(self):
		self.status = False
		self.save()
	def __str__(self):
		return self.descricao


class Noticia(models.Model):
	autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	area = models.ForeignKey(Area, on_delete=models.CASCADE)
	foto = models.ImageField(upload_to='imagens/', null=True, blank=True)
	titulo = models.CharField(max_length=200)
	texto = models.TextField()
	data_publicacao = models.DateTimeField(null=True, blank=True)

	def publicar(self):
		self.data_publicacao = timezone.now()
		self.save()
	def __str__(self):
		return self.titulo