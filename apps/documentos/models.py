from django.db import models
from apps.funcionarios.models import funcionario


class documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(funcionario, on_delete=models.PROTECT)


    def __str__(self):
        return self.descricao

