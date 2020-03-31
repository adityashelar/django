from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import sendMoney

urlpatterns = [
    path('sendMoney/', sendMoney, name='Send_Money')
    # path('requestMoney/',requestMoney, name='Request_Money')
]