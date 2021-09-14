from django.views.generic import CreateView
from .models import Documento


# Create your views here.
class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']
