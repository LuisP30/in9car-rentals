from django.contrib import messages
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse
from .forms import RegisterForm


def cadastro_view(request):
    formulario_dados = request.session.get('formulario_dados', None)
    form = RegisterForm(formulario_dados)
    return render(request, 'authen/pages/cadastro.html', {
        'form': form,
        'form_action': reverse('authen:cadastro_create'),
    })
