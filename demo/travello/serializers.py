from rest_framework import serializers
from .models import Destination , DestinationDetails

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        # fields = ['id', 'desc', 'name', 'price']
        fields = '__all__'

class DestinationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationDetails
        fields = '__all__'