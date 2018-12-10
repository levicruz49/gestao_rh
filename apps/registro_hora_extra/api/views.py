from rest_framework import viewsets
from apps.registro_hora_extra.api.serializers import RegistroHoraExtraSerializer
from apps.registro_hora_extra.models import registroHoraExtra
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

##API##
class RegistroHoraExtra_ViewSet(viewsets.ModelViewSet):
    queryset = registroHoraExtra.objects.all()
    serializer_class = RegistroHoraExtraSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )