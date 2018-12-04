from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

from apps.departamentos.models import departamento
from apps.empresas.models import Empresa

# Create your models here.

class funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamento = models.ManyToManyField(departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)
    imagem = models.FileField(upload_to='imagem_func')

    def __str__(self):
        return self.nome

    @property
    def total_horas_extra(self):
        total = self.registrohoraextra_set.filter(utilizada=False).aggregate(
            Sum('horas'))['horas__sum']
        return total or 0

    objects = models