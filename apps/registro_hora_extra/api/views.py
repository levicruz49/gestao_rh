from rest_framework import viewsets
from apps.funcionarios.api.serializers import FuncionarioSerializer
from apps.funcionarios.models import funcionario

##API##
class Funcionario_ViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = funcionario.objects.all()
    serializer_class = FuncionarioSerializer