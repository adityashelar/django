from django.db import models
from customer.models import Customer

# Create your models here.

class Account(models.Model):
    account_number = models.TextField(unique= True)
    account_type = models.TextField()
    balance = models.FloatField()
    customer_id = models.ForeignKey(Customer ,  on_delete = models.SET_NULL, null = True)
