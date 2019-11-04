from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lista_atv, name='lista_atv'),
    path('create', views.create, name='create'),
    path('<int:activity_id>', views.detail, name='detail'),
]
