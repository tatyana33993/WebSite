from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=15)
    number = models.CharField(max_length=11)
    date = models.DateField()
    time = models.TimeField()
    table = models.IntegerField()
    comment = models.CharField(max_length=100)


class Tables(models.Model):
    number = models.IntegerField()
    count_seats = models.IntegerField()
