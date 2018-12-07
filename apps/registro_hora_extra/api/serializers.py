from apps.funcionarios.models import funcionario
from rest_framework import serializers



class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = funcionario
        fields = ('nome','user','departamento', 'empresa', 'imagem')

