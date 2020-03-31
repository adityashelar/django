from rest_framework import serializers
from .models import Customer
from accounts.serializers import AccountSerializer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'