from django.shortcuts import render
from .models import Destination
from .serializers import DestinationSerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse , HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

def index(request):
    citys = Destination.objects.all()
    return render(request,'index.html', {"dest" : citys})


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
            print('inside if = ==================')
            return self.retrieve(request, id)
        else:
            print('inside else = ==================')
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


class DestinationUpdateAPIView(APIView):

    def get_Object(self, id):
        try:
            return Destination.objects.get(id = id)
        except Destination.DoesNotExist:
            return Response(status= status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        dest = self.get_Object(id)
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
        dest = Destination.objects.all()
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
