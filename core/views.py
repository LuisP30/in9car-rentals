from django.shortcuts import render

def home(request):
    return render(request,'space/pages/home.html')

def resultados(request):
    return render(request,'space/pages/resultados.html')

def detalhes(request):
    return render(request,'space/pages/detalhes.html')
