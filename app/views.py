from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Producer
from .models import Transporters
from .models import Owner
from .models import Wood
from .serializers import ProducerSerializer
from .serializers import TransportersSerializer
from .serializers import OwnerSerializer
from .serializers import WoodSerializer
def home(requets):
    return render(requets,'home.html')

class Producer_view(APIView):
    @api_view(['GET'])
    def getData(request):
        users = Producer.objects.all()
        serializer = ProducerSerializer(users, many=True)
        return Response(serializer.data)
    @api_view(['GET'])
    def getId(request, pk):
        users = Producer.objects.get(id=pk)
        serializer = ProducerSerializer(users, many=False)
        return Response(serializer.data)
    @api_view(['POST'])
    def add(request):
        serializer = ProducerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    @api_view(['PUT'])
    def update(request, pk):
        user = Producer.objects.get(id=pk)
        serializer = ProducerSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    @api_view(['DELETE'])
    def delete(request, pk):
        user = Producer.objects.get(id=pk)
        user.delete()
        return Response('User successfully deleted!')
    
   

class Transporters_view(APIView):
    @api_view(['GET'])
    def getData(request):
        users = Transporters.objects.all()
        serializer = TransportersSerializer(users, many=True)
        return Response(serializer.data)
    @api_view(['GET'])
    def getId(request, pk):
        users = Transporters.objects.get(id=pk)
        serializer = TransportersSerializer(users, many=False)
        return Response(serializer.data)
    @api_view(['POST'])
    def add(request):
        serializer = TransportersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    @api_view(['PUT'])
    def update(request, pk):
        user = Transporters.objects.get(id=pk)
        serializer = TransportersSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    @api_view(['DELETE'])
    def delete(request, pk):
        user = Transporters.objects.get(id=pk)
        user.delete()
        return Response('User successfully deleted!')

class Owner_view(APIView):
    @api_view(['GET'])
    def getData(request):
        users = Owner.objects.all()
        serializer = OwnerSerializer(users, many=True)
        return Response(serializer.data)
    @api_view(['GET'])
    def getId(request, pk):
        users = Owner.objects.get(id=pk)
        serializer = OwnerSerializer(users, many=False)
        return Response(serializer.data)
    @api_view(['POST'])
    def add(request):
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    @api_view(['PUT'])
    def update(request, pk):
        user = Owner.objects.get(id=pk)
        serializer = OwnerSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    @api_view(['DELETE'])
    def delete(request, pk):
        user = Owner.objects.get(id=pk)
        user.delete()
        return Response('User successfully deleted!')
    
class Wood_view(APIView):
    @api_view(['GET'])
    def getData(request):
        users = Wood.objects.all()
        return HttpResponse(users)
    @api_view(['GET'])
    def getId(request, pk):
        users = Wood.objects.get(id=pk)
        return HttpResponse(users)
    @api_view(['POST'])
    def add(request):
        serializer = WoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    @api_view(['PUT'])
    def update(request, pk):
        user = Wood.objects.get(id=pk)
        serializer = WoodSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    @api_view(['DELETE'])
    def delete(request, pk):
        user = Wood.objects.get(id=pk)
        user.delete()
        return Response('User successfully deleted!')