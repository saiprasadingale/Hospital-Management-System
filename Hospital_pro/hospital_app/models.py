from django.db import models


class Hospital(models.Model):
    doctor_id = models.IntegerField()
    doctor_name = models.CharField(max_length=50)
    fees = models.FloatField()
    appointment_date = models.CharField(max_length=10)
    appointment_time = models.CharField(max_length=10)
