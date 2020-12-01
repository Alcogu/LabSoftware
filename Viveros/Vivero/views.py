from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView
from .models import Vivero
from .forms import DepartamentoMunicipioVivero, FormularioVivero, FormularioMunicipio, FormularioDepartamento

class ViveroCreateView(CreateView):
    model = Vivero
    form_class = FormularioVivero
    template_name = 'vivero/viveroFormulario.html'
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