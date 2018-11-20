from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import funcionario

# Create your views here.

class funcionarioslist(LoginRequiredMixin, ListView):
    model = funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return funcionario.objects.filter(empresa=empresa_logada)

class funcionarioEdit(LoginRequiredMixin, UpdateView):
    model = funcionario
    fields = ['nome', 'departamento']
    success_url = reverse_lazy('list_funcionarios')


class funcionarioDelete(LoginRequiredMixin, DeleteView):
    model = funcionario
    success_url = reverse_lazy('list_funcionarios')

class funcionarioCreate(LoginRequiredMixin, CreateView):
    model = funcionario
    fields = ['nome', 'departamento']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(funcionarioCreate, self).form_valid(form)

    success_url = reverse_lazy('list_funcionarios')

