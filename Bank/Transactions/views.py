from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from customer.models import Customer
from accounts.models import Account
from accounts.serializers import AccountSerializer

@api_view(['POST'])
def sendMoney(request):
    amount = request.POST.get('amount')
    senderId = request.POST.get('senderId')
    recieverId = request.POST.get('recieverId')
    senderAccountId = request.POST.get('senderAccountId')
    recieverAccountId = request.POST.get('recieverAccountId')


    print('reciever Id*********************' , recieverAccountId)
    print('sender Id*************************' , senderAccountId)
    try:
        sender = Customer.objects.get(id = senderId)
        reciever = Customer.objects.get(id = recieverId)

    except Customer.DoesNotExist:
        return Response('No user found ', status= status.HTTP_204_NO_CONTENT)
    senderAccount = Account.objects.get(account_number = senderAccountId, customer_id = sender)
    recieverAccount = Account.objects.get(account_number = recieverAccountId, customer_id = reciever)

    senderAccount.balance = senderAccount.balance - float(amount)
    recieverAccount.balance = recieverAccount.balance + float(amount) 

    senderAccount.save()
    recieverAccount.save()

    serializer = AccountSerializer(senderAccount)
    return Response(serializer.data, status= status.HTTP_200_OK)