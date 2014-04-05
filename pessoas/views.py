from django.shortcuts import render, HttpResponseRedirect
from pessoas.models import Pessoa

def index(request):
    return render(request, 'index.html')