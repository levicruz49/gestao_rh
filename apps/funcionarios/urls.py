from django.urls import path
from .views import funcionarioslist

urlpatterns = [
    path('', funcionarioslist.as_view(), name='list_funcionarios'),

]