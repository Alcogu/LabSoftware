from django.shortcuts import render

# Create your views here.
def productor(request):
    return render(request, "productor/productores.html")