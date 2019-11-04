from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Activity

# Create your views here.

# Define lista_atv.
def lista_atv(request):
    activities = Activity.objects
    return render(request, 'atv_lista.html', {'activities':activities})

# Define create.
@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['activity_type'] and request.POST['code'] and request.POST['description']:
            activity = Activity()
            activity.activity_type = request.POST['activity_type']
            activity.code = request.POST['code']
            activity.description = request.POST['description']
            activity.use = request.POST['use']
            activity.save()
            return redirect('/activity/')
        else:
            return render(request, 'atv_lista.html', {'error':'Tipo, Código e Descrição são obrigatórios'})
    else:
        return render(request, 'atv_lista.html')

# Define detail.
def detail(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    return render(request, 'atv_detail.html', {'activity':activity})
