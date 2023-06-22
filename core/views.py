from django.shortcuts import render

def home(request):
    return render(request,'space/pages/home.html')

# Create your views here.
