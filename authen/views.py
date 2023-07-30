from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm


def cadastro_view(request):
    formulario_dados = request.session.get('formulario_dados', None)
    form = RegisterForm(formulario_dados)
    return render(request, 'authen/pages/cadastro.html', {
        'form': form,
        'form_action': reverse('authen:cadastro_create'),
    })


def cadastro_create(request):
    if not request.POST:
        raise Http404()
    POST = request.POST
    request.session['formulario_dados'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Cadastrado realizado com sucesso. Faça Login') # noqa

        del (request.session['formulario_dados'])

    return redirect('authen:cadastro')
