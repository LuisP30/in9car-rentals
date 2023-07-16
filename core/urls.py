from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name="home"),
    path('resultados', views.resultados, name="resultados"),
    path('detalhes', views.detalhes, name="detalhes"),

]
