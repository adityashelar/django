from django.urls import include, path
from .views import CustomersGenerics
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('customer',CustomersGenerics)

urlpatterns = [
    path('', include(router.urls))
]