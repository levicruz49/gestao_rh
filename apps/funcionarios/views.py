import io

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.views.generic.base import View
from .models import funcionario
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa


# Create your views here.

class funcionarioslist(LoginRequiredMixin, ListView):
    model = funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return funcionario.objects.filter(empresa=empresa_logada)

class funcionarioEdit(LoginRequiredMixin, UpdateView):
    model = funcionario
    fields = ['nome', 'departamento', 'imagem']
    success_url = reverse_lazy('list_funcionarios')


class funcionarioDelete(LoginRequiredMixin, DeleteView):
    model = funcionario
    success_url = reverse_lazy('list_funcionarios')

class funcionarioCreate(LoginRequiredMixin, CreateView):
    model = funcionario
    fields = ['nome', 'departamento', 'imagem']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(funcionarioCreate, self).form_valid(form)

    success_url = reverse_lazy('list_funcionarios')

#COMEÇO DA CRIAÇÃO DE PDF

class Render:
    @staticmethod

    def render(path: str, params: dict,filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)

        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' %filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Pdf(View):
    def get(self, request):
        params = {
            'today':'Variavel today',
            'sales':'Variavel sales',
            'request':request,
        }
        return Render.render('funcionarios/relatorio.html', params, 'myfile')

