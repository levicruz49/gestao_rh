from django.db import models
from apps.funcionarios.models import funcionario

class registroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.motivo