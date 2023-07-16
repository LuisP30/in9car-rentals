from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

class Veiculo(models.Model):
    MANUAL = 'M'
    AUTOMATICO = 'A'
    cambio_veiculo_choices = (
        (MANUAL, 'Manual'),
        (AUTOMATICO, 'Automatico'),
    )

    modelo = models.CharField(max_length=45)
    marca = models.CharField(max_length=15)
    placa = models.CharField(max_length=7)
    renavam = models.CharField(max_length=20)
    capacidade = models.IntegerField()
    cambio = models.CharField(max_length=1, choice=cambio_veiculo_choices)
    combustivel = models.CharField(max_length=45)
    potencia = models.CharField(max_length=45)
    cor = models.CharField(max_length=12)
    ano = models.CharField(max_length=4)
    disponivel = models.BooleanField(default=False)
    imagem = models.ImageField(upload_to='core/covers/%Y/%m/%d/')
    valor = models.DecimalField(max_digits=5, decimal_places=2)
