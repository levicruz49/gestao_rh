import csv
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import registroHoraExtra
from .forms import RegistroHoraExtra
import xlwt


# Create your views here.

class horaextralist(LoginRequiredMixin, ListView):
    model = registroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return registroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class horaextracreate(LoginRequiredMixin, CreateView):
    model = registroHoraExtra
    form_class = RegistroHoraExtra

    def get_form_kwargs(self):
        kwargs = super(horaextracreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    # def get_success_url(self):
    #     return reverse_lazy('update_funcionario', args=[self.object.id])

class horaextracreate_base(LoginRequiredMixin, CreateView):
    model = registroHoraExtra
    form_class = RegistroHoraExtra

    def get_form_kwargs(self):
        kwargs = super(horaextracreate_base, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    success_url = reverse_lazy('list_hora_extra')


class horaextraedit(LoginRequiredMixin, UpdateView):
    model = registroHoraExtra
    form_class = RegistroHoraExtra

    def get_form_kwargs(self):
        kwargs = super(horaextraedit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class horaextraedit_base(LoginRequiredMixin, UpdateView):
    model = registroHoraExtra
    form_class = RegistroHoraExtra

    def get_form_kwargs(self):
        kwargs = super(horaextraedit_base, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    success_url = reverse_lazy('list_hora_extra')

class horaextradelet(LoginRequiredMixin, DeleteView):
    model = registroHoraExtra
    success_url = reverse_lazy('list_hora_extra')


class utilizouHoraExtra(View):
    def post(self, *args, **kwargs):

        registro_hora_extra = registroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = True
        registro_hora_extra.save()

        empregado = self.request.user.funcionario

        response = json.dumps({'mensagem': 'Requisição executada',
                               'horas': float(empregado.total_horas_extra)
                               }),

        return HttpResponse(response, content_type='application/json')

class horaextraRelatorio(View):

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        registro_he = registroHoraExtra.objects.filter(utilizada=False)

        writer = csv.writer(response)
        writer.writerow(['ID', 'Motivo', 'Funcionario', 'Horas Restantes', 'Horas'])

        for registro in registro_he:
            writer.writerow([registro.id, registro.motivo, registro.funcionario,
                             registro.funcionario.total_horas_extra, registro.horas

            ])

        return response

class horaextraRelatorio_Excel(View):

    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="relatorio.xls"'

        wb = xlwt.Workbook(encoding='utf-u')
        ws= wb.add_sheet('Banco de horas')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['ID', 'Motivo', 'Funcionario', 'Horas Restantes', 'Horas']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        registro_he = registroHoraExtra.objects.filter(utilizada=False)

        row_num = 1
        for registro in registro_he:
            ws.write(row_num, 0, registro.id, font_style)
            ws.write(row_num, 1, registro.motivo, font_style)
            ws.write(row_num, 2, registro.funcionario.nome, font_style)
            ws.write(row_num, 3, registro.funcionario.total_horas_extra, font_style)
            ws.write(row_num, 4, registro.horas, font_style)

            row_num += 1
        wb.save(response)

        return response