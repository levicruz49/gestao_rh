from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import departamento



class DepartamentoList(LoginRequiredMixin, ListView):
    model = departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return departamento.objects.filter(empresa=empresa_logada)

class DepartamentoCreate(LoginRequiredMixin, CreateView):
    model = departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoCreate, self).form_valid(form)

    success_url = reverse_lazy('list_departamento')

class DepartamentoUpdate(LoginRequiredMixin, UpdateView):
    model = departamento
    fields = ['nome']
    success_url = reverse_lazy('list_departamento')

class DepartamentoDelete(LoginRequiredMixin, DeleteView):
    model = departamento
    success_url = reverse_lazy('list_departamento')