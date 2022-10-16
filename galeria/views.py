from django.shortcuts import render
from django.http import HttpResponse

"""
#aqui criamos um função que ira retornar o html especificado quando for chamada
##ela foi expecificada no urls.py
def index(request):
    return HttpResponse('<h1>olá mundo</h1>')
"""

#forma certa é usando o render

def index(request):
    return render(request, 'galeria/index.html')

def image(request):
    return render(request, 'galeria/image.html')