from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountsViewSet , getUserAccounts, addUserAccount

router = DefaultRouter()
router.register('account',AccountsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('getUserAccount/<int:id>/', getUserAccounts, name= 'Get_user_Accounts'),
    path('addUserAccount/<int:id>',addUserAccount, name= 'Add_user_Account')
]