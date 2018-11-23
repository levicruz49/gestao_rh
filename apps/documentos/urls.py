from django.urls import path
from .views import documentoCreate#, documentoDelete


urlpatterns = [
    path('novo/<int:funcionario_id>/', documentoCreate.as_view(), name='create_documento'),
    # path('deletar/<int:pk>', documentoDelete.as_view(), name='delete_documento'),


]