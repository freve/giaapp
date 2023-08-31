from django.shortcuts import render
from noticias.models import Publicacion

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def index(request):
    listaNoticias = Publicacion.objects.filter(tipoEvento='N').order_by("orden", "-fecha_realizacion")[:6]
    listaEventos = Publicacion.objects.filter(tipoEvento='E').order_by("orden", "-fecha_realizacion")[:6]

    return render(request, 'index.html', {'listaNoticias': listaNoticias, 'listaEventos': listaEventos})

def servicios(request):
    return render(request, 'services.html')

def lineas(request):
    return render(request, 'lineas.html')

def proyectos(request):
    return render(request, 'proyectos.html')

def team(request):
    return render(request, 'team.html')

def semilleros(request):
    return render(request, 'semilleros.html')

def contacto(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')