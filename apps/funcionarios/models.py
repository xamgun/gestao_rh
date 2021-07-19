from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from apps.departamentos.models import Departamento
from apps.empresas.models import Empresas

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresas, on_delete=models.PROTECT,
                                null=True, blank=True)

    def get_absolute_url(self):
        return reverse('list_funcionarios')

    def __str__(self):
        return self.nome

