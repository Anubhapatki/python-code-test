from django.shortcuts import render
from .models import Starship
from .serializer import StarShipSerializer
from rest_framework import generics

# Create your views here.
class StarshipAPIListView(generics.ListAPIView):
    queryset = Starship.objects.all()
    serializer_class = StarShipSerializer
