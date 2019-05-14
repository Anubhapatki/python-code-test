from django.shortcuts import render
from .models import Starship, Listing
from .serializer import StarShipSerializer, ListingSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from django.http import Http404
from rest_framework import status


# Create your views here.
class StarshipAPIListView(generics.ListAPIView):
    queryset = Starship.objects.all()
    serializer_class = StarShipSerializer



class StarshipClassListView(APIView):

    def get(self, request, starship_class, format=None):
        starships_per_class = Starship.objects.filter(starship_class=starship_class)
        serializer = StarShipSerializer(starships_per_class, many=True)
        return Response(serializer.data)



class StarshipListing(generics.ListCreateAPIView):
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('price', 'creation_time')

    def perform_create(self, serializer):
        q = serializer.save()



class StarshipListingDetail(APIView):


    def get_object(self,id):
        try:
            return Listing.objects.get(pk=id)
        except Listing.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        listing = self.get_object(id)
        serializer = ListingSerializer(listing)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        listing = self.get_object(id)
        serializer = ListingSerializer(listing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

