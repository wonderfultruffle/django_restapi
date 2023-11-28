from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Booking
from .serializers import BookingSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.
# API 뷰
class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# API 뷰
class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer