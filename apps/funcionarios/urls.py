from django.urls import path
from .views import FuncionariosList, FuncionariosEdit, FuncionariosDelete


urlpatterns = [
    path('funcionarios', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>', FuncionariosEdit.as_view(), name='update_funcionarios'),
    path('deletar/<int:pk>', FuncionariosDelete.as_view(), name='delete_funcionarios'),
]
