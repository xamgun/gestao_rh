from django.db import models
from apps.empresas.models import Empresas


# Create your models here.
class Departamento(models.Model):
    nome = models.CharField(max_length=70)
    empresa = models.ForeignKey(Empresas, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


