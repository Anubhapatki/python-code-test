from rest_framework import serializers
from .models import Starship


class StarShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Starship
        fields = "__all__"
