from django.shortcuts import render
from django.http import HttpResponse
import subprocess

# Create your views here.

def index(request):
    return render(request, 'ping.html')

def Busqueda(request):

    if 'host' in request.GET:
        
        host = request.GET['host']
        ping = subprocess.Popen(
               ["ping", "-c", "1", host],
               stdout = subprocess.PIPE ,
               stderr = subprocess.PIPE)

        out, error = ping.communicate()
        if out:
            return HttpResponse("El sitio %s esta disponible." % host)
        else:
            return HttpResponse("El sitio %s no responde." % host)

    else:
        return HttpResponse("Por favor introduce un host valido")
