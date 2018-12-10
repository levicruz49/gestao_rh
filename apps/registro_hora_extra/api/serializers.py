from rest_framework import serializers
from apps.registro_hora_extra.models import registroHoraExtra



class RegistroHoraExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = registroHoraExtra
        fields = ('motivo','funcionario','horas', 'utilizada')

