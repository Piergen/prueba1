from django.shortcuts import render

# Create your views here.

def mostrar_index(request):
    return render(request,'App2/index.html')