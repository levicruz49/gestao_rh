from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa

class EmpresaCreate(LoginRequiredMixin, CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('ok')



class EmpresaEdit(LoginRequiredMixin, UpdateView):
    model = Empresa
    fields = '__all__'
    success_url = reverse_lazy('home')