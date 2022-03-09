from dataclasses import fields
from .models import RegistroHoraExtra
from django.views.generic import (ListView, UpdateView)

# Create your views here.
class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)

class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra

    fields = ['motivo', 'funcionario', 'horas']



