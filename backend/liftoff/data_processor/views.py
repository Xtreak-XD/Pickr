from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import techItems, carParts, toys, clothesItems, forYouPage
from .serializer import automotiveSerializer, techItemSerializer, toysSerializer, clothesSerializer, forYouPageSerializer

@api_view(['GET'])
def get_automotives(request):
    data = carParts.objects.all()
    serializer = automotiveSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_techItems(request):
    data = techItems.objects.all()
    serializer = techItemSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_toys(request):
    data = toys.objects.all()
    serializer = toysSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_clothes(request):
    data = clothesItems.objects.all()
    serializer = clothesSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_FYP(request):
    data = forYouPage.objects.all()
    serializer = forYouPageSerializer(data, many=True)
    return Response(serializer.data)
