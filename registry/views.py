from django.shortcuts import render
from .models import Registry, Preceptor

# Create your views here.
def lista_prec(request):
    preceptores = Preceptor.objects
    return render(request, 'prec_lista.html', {'preceptores':preceptores})
