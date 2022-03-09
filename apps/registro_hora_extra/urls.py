from django.urls import path
from .views import (
    HoraExtraList,
    HoraExtraEdit
)


urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('editar/<int:pk>', HoraExtraEdit.as_view(), name='update_hora_extra')
    # path('deletar/<int:pk>', FuncionariosDelete.as_view(), name='delete_funcionarios'),
    # path('novo', FuncionariosNovo.as_view(), name='create_funcionarios'),
]
