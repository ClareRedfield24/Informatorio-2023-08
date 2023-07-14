from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("La Recetas Mas faciles del mundo")

# Create your views here.
