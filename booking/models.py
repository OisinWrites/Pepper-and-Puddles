from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)

class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    available = models.BooleanField(default=True)