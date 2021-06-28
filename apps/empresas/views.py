from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Empresas


# Create your views here.
class EmpresaCreate(CreateView):
    model = Empresas
    fields = ['nome']