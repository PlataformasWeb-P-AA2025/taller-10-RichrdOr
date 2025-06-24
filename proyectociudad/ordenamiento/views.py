from django.shortcuts import render

from .models import Parroquia, Ciudadela
# Create your views here.

def listar_parroquias(request):
    parroquias = Parroquia.objects.all()
    return render(request, 'listar_parroquias.html', {'parroquias': parroquias})