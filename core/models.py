from django.db import models


class Veiculo(models.Model):
    class cambioVeiculo(models.TextChoices):
        MANUAL = 'M',
        AUTOMATICO = 'A',

    modelo = models.CharField(max_length=45)
    marca = models.CharField(max_length=15)
    placa = models.CharField(max_length=7)
    renavam = models.CharField(max_length=20)
    capacidade = models.PositiveIntegerField()
    combustivel = models.CharField(max_length=45)
    potencia = models.CharField(max_length=45)
    cor = models.CharField(max_length=12)
    ano = models.CharField(max_length=4)
    disponivel = models.BooleanField(default=False)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    cambio = models.CharField(max_length=1, choices=cambioVeiculo.choices)
    cover = models.ImageField(upload_to='core/covers/%Y/%m/%d/', blank=False)
