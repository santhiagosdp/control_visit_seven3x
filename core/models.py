from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class visitante(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    data = models.DateTimeField(auto_now=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    celular = models.CharField(max_length=100)
    fone = models.CharField(max_length=100)
    #endereço
    cep = models.CharField(max_length=20)
    endereco = models.CharField(max_length=150)
    complemento = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class visita(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    data = models.DateTimeField(auto_now=True)
    visitante = models.ForeignKey(visitante, on_delete=models.PROTECT)
    descricao = models.TextField(max_length=5000)

    def __str__(self):
        return self.descricao
