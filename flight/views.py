from rest_framework.viewsets import ModelViewSet
from .serializers import (
    PassengerSerializer,
    FlightSerializer,
    ReservationSerializer,
    Passenger,
    Flight,
    Reservation,
)


class FixView(ModelViewSet):
    pass


class PassengerView(FixView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class FlightView(FixView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class ReservationView(FixView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


