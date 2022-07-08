from distutils.command.upload import upload
from time import timezone
from django.utils import timezone
from django.db import models

class Categoria(models.Model):
  nome = models.CharField(max_length=255)

  def __str__(self):
    return self.nome

class Contato(models.Model):
  nome = models.CharField(max_length=255)
  sobrenome = models.CharField(max_length=255, blank=True)
  telefone = models.CharField(max_length=255)
  email = models.CharField(max_length=255, blank=True)
  data_criação = models.DateTimeField(default=timezone.now)
  descrição = models.TextField(blank=True)
  categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
  mostrar = models.BooleanField(default=True)
  foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')

  def __str__(self):
    return self.nome

  