from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import funcionario

# Create your views here.

class funcionarioslist(ListView):
    model = funcionario