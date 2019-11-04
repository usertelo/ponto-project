from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    Teórico = 'T'
    Teórico_Prático = 'TP'
    Prático = 'P'
    activity_type_choices = [
        (Teórico, 'Teórico'),
        (Teórico_Prático, 'Teórico-Prático'),
        (Prático, 'Prático'),
    ]
    activity_type = models.CharField(max_length=2, choices=activity_type_choices)
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    use = models.TextField(default='vazio')
    # ementa: procurar field para upload PDF

    def __str__(self):
        return self.code + " " + self.description
