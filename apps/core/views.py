from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.funcionarios.models import Funcionario


# Create your views here.
@login_required
def home(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'core/index.html', data)
