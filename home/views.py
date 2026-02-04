from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home/home.html')

def tuna(request):
    return render(request, 'home/tuna.html')

def coral(request):
    return render(request, 'home/coral.html')

def tbd(request):
    return render(request, 'home/tbd.html')
