from django.urls import path, re_path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework import permissions

router = DefaultRouter()
router.register('viewset',views.DestinationViewSet)
router.register('details', views.DestinationDetialsViewSet)

urlpatterns = [
    path('',views.index,name="index"),
    path('dest/',include(router.urls)),
    # path('getAll', views.getDestination, name = "destinations"),
    path('getAll', views.DestinationAPIView.as_view(),name = "destinations"),
    re_path(r'^generics/(?:(?P<id>[1-9]+)/)?', views.DestinationsGenerics.as_view(),name = "generics"),
    path('update/<int:id>/',views.DestinationUpdateAPIView.as_view(), name = 'updatedestinations'),
    path('filters/', views.getDestination),
    path('updateDestinations/<int:pk>', views.updateDestinations)
]