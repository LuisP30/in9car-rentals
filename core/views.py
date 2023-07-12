from django.shortcuts import render, get_list_or_404, get_object_or_404


def home(request):
    return render(request,'space/pages/home.html')

def resultados(request, id):
    veiculo = Veiculo.objects.filter(is_published = True).order_by('-id')
    return render(request, 'space/pages/resultados.html', context={
        'veiculo' : veiculo,

    })
