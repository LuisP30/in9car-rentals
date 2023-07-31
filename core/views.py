from django.shortcuts import render
from .models import Veiculo


def home(request):
    return render(request, 'space/pages/home.html')


def resultados(request):
    veiculos = Veiculo.objects.filter(disponivel=True).order_by('-id')
    return render(request, 'space/pages/resultados.html', context={
        'veiculos': veiculos,
    })


def detalhes(request):
    return render(request, 'space/pages/detalhes.html')
