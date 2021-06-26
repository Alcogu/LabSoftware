from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView
from .models import Vivero
#from .forms import DepartamentoMunicipioVivero, FormularioVivero, FormularioMunicipio, FormularioDepartamento
from .forms import *

class ViveroCreateView(CreateView):
    model = Vivero
    form_class = FormularioVivero
    template_name = 'vivero/viveroFormulario.html'
    #form_class = FormularioVivero
    #second_form_class = FormularioMunicipio
    #third_form_class = FormularioMunicipio
    #queryset = Vivero.objects.filter()
    success_url = reverse_lazy('vivero:listar_vivero')

class ListarVivero(ListView):
    model = Vivero
    template_name = "vivero/tablaViveros.html"

class EditarVivero(UpdateView):
    model = Vivero
    template_name = "vivero/viveroFormulario.html"
    form_class = FormularioVivero
    success_url = reverse_lazy('vivero:listar_vivero')

class EliminarVivero(DeleteView):
    model = Vivero
    success_url = reverse_lazy('vivero:listar_vivero')
