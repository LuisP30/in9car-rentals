from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name= 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('resultados', views.resultados, name='resultados'),

    
    path('login/', LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),


]
