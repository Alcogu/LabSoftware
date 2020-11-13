from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from forms import FormularioProductor

# Create your views here.
def productor(request):
    return render(request, "productor/productores.html")

#La vista es la que recibe la petición y la ejecuta.
'''
#Vista para el formulario 
def productorFormulario(request):
    if request.method == 'POST':
        form = FormularioProductor(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')
    else:
        form = FormularioProductor()
    return render(request, '', {'form': form})


def gracias(request):
    html = '<html><body>"Gracias por enviar los datos.</body></html>'
    return HttpResponse(html)'''
