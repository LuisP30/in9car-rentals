from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name="home"),
    path('core/resultados', views.resultados, name="resultados"),
    path('core/detalhes', views.detalhes, name="detalhes"),

]
