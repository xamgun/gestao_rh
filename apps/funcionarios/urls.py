from django.urls import path
from .views import FuncionariosList


urlpatterns = [
    path('', FuncionariosList.as_view(), name='funcionarios_list')
]
