from django.shortcuts import render, get_list_or_404, get_object_or_404


def home(request):
    return render(request,'space/pages/home.html')

def resultados(request):
    return render(request,'space/pages/resultados.html')

def detalhes(request):
    return render(request,'space/pages/detalhes.html')
