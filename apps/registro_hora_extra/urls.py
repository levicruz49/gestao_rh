from django.urls import path
from .views import horaextralist



urlpatterns = [
    path('', horaextralist.as_view(), name='list_hora_extra'),
    # path('novo/', funcionarioCreate.as_view(), name='create_funcionario'),
    # path('editar/<int:pk>', funcionarioEdit.as_view(), name='update_funcionario'),
    # path('deletar/<int:pk>', funcionarioDelete.as_view(), name='delete_funcionario'),


]