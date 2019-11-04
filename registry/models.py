from django.db import models
from django.contrib.auth.models import User
from activity.models import Activity

class Preceptor(models.Model):
    prec_code = models.CharField(max_length=10)
    prec_name = models.CharField(max_length=100)

    def __str__(self):
        return self.prec_code + " " + self.prec_name

class Registry(models.Model):
    reg_date = models.DateField()
    reg_activity_code = Activity.code
    reg_activity_description = Activity.description
    reg_ch = models.IntegerField()
    reg_preceptor_code = Preceptor.prec_code
    reg_preceptor_name = Preceptor.prec_name
