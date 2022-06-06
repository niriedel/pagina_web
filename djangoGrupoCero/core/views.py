from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'core/index.html')

def login(request):

    return render(request, 'core/acceso/login/index.html')

def register(request):

    return render(request, 'core/acceso/register/index.html')

