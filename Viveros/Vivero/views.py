from django.shortcuts import render

# Create your views here.

def vivero(request):
    return render(request, "vivero/viveroFormulario.html")