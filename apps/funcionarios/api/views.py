from rest_framework import viewsets
from apps.funcionarios.api.serializers import FuncionarioSerializer
from apps.funcionarios.models import funcionario
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

##API##
class Funcionario_ViewSet(viewsets.ModelViewSet):
    queryset = funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
