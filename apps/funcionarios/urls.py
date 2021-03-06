from django.urls import path
from .views import funcionarioslist, funcionarioEdit, \
    funcionarioDelete, funcionarioCreate, Pdf



urlpatterns = [
    path('', funcionarioslist.as_view(), name='list_funcionarios'),
    path('novo/', funcionarioCreate.as_view(), name='create_funcionario'),
    path('editar/<int:pk>/', funcionarioEdit.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>/', funcionarioDelete.as_view(), name='delete_funcionario'),
    path('relatorio_funcionarios/', Pdf.as_view(), name='relatorio_funcionarios'),


]