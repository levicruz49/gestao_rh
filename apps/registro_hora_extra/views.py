from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import registroHoraExtra

# Create your views here.

class horaextralist(ListView):
    model = registroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return registroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)