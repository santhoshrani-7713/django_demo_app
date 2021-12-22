from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class LineA(models.Model):
    # identity = models.AutoField(primary_key=True)
    shift_model = models.IntegerField(primary_key=True)
    std_shift_time_gross = models.IntegerField()
    start_up = models.IntegerField()
    break_time = models.IntegerField()
    lunch = models.IntegerField()
    other = models.IntegerField()
    # std_shift_time =  models.IntegerField(default=470)
    days_or_week = models.IntegerField()
    weeks_per_year = models.IntegerField(default = 50)

    def __str__(self):
        return str(self.shift_model)

class LineB(models.Model):
    # identity = models.AutoField(primary_key=True)
    shift_model = models.IntegerField(primary_key=True)
    std_shift_time_gross = models.IntegerField()
    start_up = models.IntegerField()
    break_time = models.IntegerField()
    lunch = models.IntegerField()
    other = models.IntegerField()
    # std_shift_time =  models.IntegerField(default=470)
    days_or_week = models.IntegerField()
    weeks_per_year = models.IntegerField(default = 50)

    def __str__(self):
        return str(self.shift_model)