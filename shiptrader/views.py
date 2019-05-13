from django.shortcuts import render
from .models import Starship, Listing
from .serializer import StarShipSerializer, ListingSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters


# Create your views here.
class StarshipAPIListView(generics.ListAPIView):
    queryset = Starship.objects.all()
    serializer_class = StarShipSerializer


class StarshipClassListView(generics.ListAPIView):

    serializer_class = StarShipSerializer

    def get_queryset(self):
        starship_class = self.kwargs.get['starship_class']
        return Starship.objects.filter(starship_class=starship_class)


class StarshipListing(generics.ListCreateAPIView):
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('price', 'creation_time')

    def perform_create(self, serializer):
        q = serializer.save()

class UpdateStarshipListing(generics.UpdateAPIView):
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()
    lookup_field = 'id'

