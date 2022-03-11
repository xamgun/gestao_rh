from dataclasses import fields
from pyexpat import model

from django.urls import reverse_lazy
from .models import RegistroHoraExtra
from django.views.generic import (ListView, UpdateView, DeleteView)

# Create your views here.
class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra

    fields = ['motivo', 'funcionario', 'horas']


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')



