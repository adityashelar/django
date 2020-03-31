from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')

class DestinationDetails(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    city = models.ForeignKey(Destination, on_delete = models.CASCADE) 