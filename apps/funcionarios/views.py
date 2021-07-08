from django.views.generic import ListView
from .models import Funcionario


# Create your views here.
class FuncionariosList(ListView):
    model = Funcionario



