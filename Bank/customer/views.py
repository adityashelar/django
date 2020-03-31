from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import APIView
import logging

logging.basicConfig(level=logging.INFO)

class CustomersGenerics(viewsets.ModelViewSet):
        logging.info('inside generics')
        queryset = Customer.objects.all()
        serializer_class = CustomerSerializer
        authentication_classes = [BasicAuthentication]
        permission_classes = [IsAuthenticated]