from django.shortcuts import render
from .models import Destination , DestinationDetails
from .serializers import DestinationSerializer, DestinationDetailsSerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse , HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
import logging
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .exceptions import *


logging.basicConfig(level= logging.INFO)

def index(request):
    citys = Destination.objects.all()
    return render(request,'index.html', {"dest" : citys})


class DestinationViewSet(viewsets.ModelViewSet):
    serializer_class = DestinationSerializer
    queryset = Destination.objects.all()


class DestinationsGenerics(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin
                    , mixins.UpdateModelMixin, mixins.DestroyModelMixin) :


    serializer_class = DestinationSerializer
    queryset = Destination.objects.all()
    lookup_field = 'id'

    # session or basic auth
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    
    #token auth generated in admin panel
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id = None):
        if id:
            logging.info('inside if = ==================')
            return self.retrieve(request, id)
        else:
            logging.info('inside else = ==================')
            return self.list(request)

    def post(self, request, id):
        return self.create(request)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request,id)

class DestinationAPIView(APIView):

    def get(self, request):
        data = Destination.objects.all()
        serializer = DestinationSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DestinationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])
class DestinationUpdateAPIView(APIView):

    def get_Object(self, id):
        logging.info("inside try****************************")
        return Destination.objects.get(id = id)

    @method_decorator(cache_page(60*1))
    def get(self, request, id):
        logging.info("inside get cache=======================")
        try:
            dest = self.get_Object(id)
        except:
            raise DataNotFoundException()
        serializer = DestinationSerializer(dest)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def put(self, request, id):
        dest = self.get_Object(id)
        serializer = DestinationSerializer(dest, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        dest = self.get_Object(id)
        dest.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def getDestination(request):
    if request.method == 'GET':
        dest = Destination.objects.raw("SELECT * FROM public.travello_destination where name = 'Satara'")
        serializer = DestinationSerializer(dest, many = True)
        return Response(serializer.data)
    else:
        serializer = DestinationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def updateDestinations(request, pk):
    try:
        destination = Destination.objects.get(pk = pk)
    except Destination.DoesNotExist:
        return Response(status= status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = DestinationSerializer(destination)
        return Response(serializer.data, status= status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = DestinationSerializer(destination,data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        destination.delete()
        return Response(status= status.HTTP_200_OK)


class DestinationDetialsViewSet(viewsets.ModelViewSet):
    serializer_class  = DestinationDetailsSerializer
    queryset = DestinationDetails.objects.all()