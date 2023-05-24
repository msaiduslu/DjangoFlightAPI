from rest_framework import serializers
from .models import (
    Passenger,
    Flight,
    Reservation,
)

class FixSerializer(serializers.ModelSerializer):
    pass


class PassengerSerializer(FixSerializer):

    class Meta:
        model = Passenger
        exclude=[]


class FlightSerializer(FixSerializer):
    
    class Meta:
        model = Flight
        exclude=[]


class ReservationSerializer(FixSerializer):

    class Meta:
        model = Reservation
        exclude=[]





