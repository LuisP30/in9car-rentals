from django.urls import path
from . import views

app_name = 'authen'

urlpatterns = [
    path('cadastro', views.cadastro_view, name="cadastro"),
]
