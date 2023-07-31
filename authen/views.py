from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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

        del (request.session['formulario_dados'])

    return redirect('authen:cadastro')


def login_view(request):
    form = LoginForm()
    return render(request, 'authen/pages/login.html', {
        'form': form,
        'form_action': reverse('authen:login_create')
    })


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    login_url = reverse('authen:login')

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', '')
        )
        if authenticated_user is not None:
            login(request, authenticated_user)

    return redirect(login_url)


@login_required(login_url='authen:login', redirect_field_name='next')
def logout_view(request):

    if not request.POST:
        return redirect(reverse('authen:login'))

    if request.POST.get('username') != request.user.username:
        return redirect(reverse('authen:login'))

    logout(request)
    return redirect(reverse('authen:login'))
