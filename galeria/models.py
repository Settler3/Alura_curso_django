from django.db import models
from datetime import datetime

# Create your models here.
class Categoria(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome

class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data_publicacao = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.nome