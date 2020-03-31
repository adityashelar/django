from django.shortcuts import render
from rest_framework import viewsets
from .models import Account, Customer
from .serializers import AccountSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import APIView , api_view
from rest_framework.response import Response
from rest_framework import status
import string, random
class AccountsViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
def getUserAccounts(request, id):
        data = Account.objects.filter(customer_id =id)
        serializer = AccountSerializer(data, many = True)
        return Response(serializer.data , status= status.HTTP_200_OK)

@api_view(['POST'])
def addUserAccount(request, id):
    try:
        customer = Customer.objects.get(id = id)
    except Customer.DoesNotExist:
        return Response(data = 'No user found.',status= status.HTTP_204_NO_CONTENT)
    account_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    account = Account(account_number = account_number, account_type = "saving", balance = 0.0, customer_id = customer)
    account.save()
    serializer = AccountSerializer(account)
    return Response(serializer.data, status= status.HTTP_201_CREATED)