from django.forms import ModelForm
from .models import registroHoraExtra
from apps.funcionarios.models import funcionario

class RegistroHoraExtra(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(RegistroHoraExtra, self).__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = funcionario.objects\
            .filter(empresa=user.funcionario.empresa)

    class Meta:
        model = registroHoraExtra
        fields = ['motivo', 'funcionario', 'horas']
