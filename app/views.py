from django.shortcuts import render
from rest_framework import viewsets 
from .models import * 
from .serializers import *
# Create your views here.

class MarcasView(viewsets.ModelViewSet):
    queryset = Marcas.objects.all()
    serializer_class = MarcasSerializers

class CarrosView(viewsets.ModelViewSet):
    queryset = Carros.objects.all()
    serializer_class = CarrosSerializers