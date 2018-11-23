from django.db import models
from apps.funcionarios.models import funcionario

class registroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=9, decimal_places=2)

    objects = models

    def __str__(self):
        return self.motivo