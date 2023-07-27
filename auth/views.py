from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse


def cadastro_view(request):
    return render(request, 'auth/pages/cadastro.html')


def cadastro_create(request):
    return redirect('auth:register')
