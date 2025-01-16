from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def definicje(request):
    return render(request, 'definicje.html')

def postepowanie(request):
    return render(request, 'postepowanie.html')

def ustawy(request):
    return render(request, 'ustawy.html')