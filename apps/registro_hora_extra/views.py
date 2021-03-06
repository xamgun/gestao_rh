from dataclasses import fields
from pyexpat import model

from django.urls import reverse_lazy
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm
from django.views.generic import (ListView, UpdateView, DeleteView, CreateView)

# Create your views here.
class HoraExtraList(ListView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    success_url = reverse_lazy('list_hora_extra')

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user' : self.request.user})
        return kwargs


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra

    fields = ['motivo', 'funcionario', 'horas']


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')


class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    success_url = reverse_lazy('list_hora_extra')

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user' : self.request.user})
        return kwargs



