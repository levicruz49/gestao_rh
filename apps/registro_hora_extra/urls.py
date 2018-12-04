from django.urls import path
from .views import  horaextralist, horaextracreate_base, horaextracreate,\
    horaextraedit, horaextraedit_base ,horaextradelet, utilizouHoraExtra,\
    horaextraRelatorio, horaextraRelatorio_Excel



urlpatterns = [
    path('', horaextralist.as_view(), name='list_hora_extra'),
    path('novo/', horaextracreate_base.as_view(), name='create_hora_extra_base'),
    path('novo-funcionario/', horaextracreate.as_view(), name='create_hora_extra'),
    path('editar/<int:pk>', horaextraedit_base.as_view(), name='update_hora_extra_base'),
    path('editar-funcionario/<int:pk>/', horaextraedit.as_view(), name='update_hora_extra'),
    path('utilizou-hora-extra/<int:pk>/', utilizouHoraExtra.as_view(), name='utilizou_hora_extra'),
    path('deletar/<int:pk>/', horaextradelet.as_view(), name='delete_hora_extra'),
    path('relatorio_hora_extra/', horaextraRelatorio.as_view(), name='relatorio_hora_extra'),
    path('relatorio_hora_extra_excel/', horaextraRelatorio_Excel.as_view(), name='relatorio_hora_extra_excel'),


]