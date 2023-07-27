from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('auth/login', views.login, name="login"),
    path('core/cadastro', views.cadastro, name="cadastro"),
]
