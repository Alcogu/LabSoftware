from django.shortcuts import render, redirect
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from Productor.forms import FormularioProductor
from Productor.models import Productor
from django.views.generic.edit import CreateView

# Create your views here.
def productor(request):
    if request.method == 'POST':
        form = FormularioProductor(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Productor')
    else:
        form = FormularioProductor
    return render(request, 'productor/productores.html', {'form': form})
    

