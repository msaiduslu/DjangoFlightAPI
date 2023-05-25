from rest_framework import serializers
from .models import (
    Passenger,
    Flight,
    Reservation,
)

class FixSerializer(serializers.ModelSerializer):
    created = serializers.StringRelatedField()
    created_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        validated_data['created_id'] = self.context['request'].user.id
        return super().create(validated_data)


class PassengerSerializer(FixSerializer):

    gender_text = serializers.SerializerMethodField()

    class Meta:
        model = Passenger
        exclude=[]
        
            

    def get_gender_text(self,obj):
        return obj.get_gender_display()





class FlightSerializer(FixSerializer):
    
    departure_text = serializers.SerializerMethodField()
    arrival_text = serializers.SerializerMethodField()

    class Meta:
        model = Flight
        exclude=[]

    def get_departure_text(self,obj):
        return obj.get_departure_display()
    
    def get_arrival_text(self,obj):
        return obj.get_arrival_display()


class ReservationSerializer(FixSerializer):

    # flight = serializers.StringRelatedField()
    flight = FlightSerializer(read_only=True)
    flight_id = serializers.IntegerField(write_only=True)
    passenger_ids = serializers.ListField(write_only=True)
    passenger = PassengerSerializer(many=True,read_only=True)

    class Meta:
        model = Reservation
        exclude=[]

    def create(self, validated_data):
        validated_data['passenger'] = validated_data.pop('passenger_ids')
        return super().create(validated_data)





