from django.shortcuts import render
from App1.models import familiares
# Create your views here.

def mostrar_familiares(request):
    f1 = familiares(nombre_completo="Gisella Barchiesi",edad=31,fecha_nacimiento="1991-09-28")
    f2 = familiares(nombre_completo="Martina Dominguez",edad=3,fecha_nacimiento="2019-02-11")   
    f3 = familiares(nombre_completo="Ignacio Snobohm",edad=25,fecha_nacimiento="1997-05-07")

    return render(request,'App1/familiares.html',{'familiares':[f1,f2,f3]})

def mostrar_index(request):
    return render(request,'App1/index.html')