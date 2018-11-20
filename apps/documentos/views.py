from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView, CreateView
from .models import documento

# Create your views here.

class documentoCreate(LoginRequiredMixin, CreateView):
    model = documento
    fields = ['descricao', 'arquivo']