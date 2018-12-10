from apps.funcionarios.models import funcionario
from apps.registro_hora_extra.api.serializers import RegistroHoraExtraSerializer
from rest_framework import serializers



class FuncionarioSerializer(serializers.ModelSerializer):
    registrohoraextra_set = RegistroHoraExtraSerializer(many=True)
    class Meta:
        model = funcionario
        fields = ('nome','user','departamento', 'empresa', 'imagem', 'registrohoraextra_set')

