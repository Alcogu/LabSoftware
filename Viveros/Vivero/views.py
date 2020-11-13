from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "vivero/index.html")

def vivero(request):
    return render(request, "vivero/viveroFormulario.html")