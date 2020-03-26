from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    # path('getAll', views.getDestination, name = "destinations"),
    path('getAll', views.DestinationAPIView.as_view(),name = "destinations"),
    re_path(r'^generics/(?:(?P<id>[1-9]+)/)?', views.DestinationsGenerics.as_view(),name = "generics"),
    path('update/<int:id>/',views.DestinationUpdateAPIView.as_view(), name = 'updatedestinations')

]