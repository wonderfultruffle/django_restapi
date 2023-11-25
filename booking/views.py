from django.shortcuts import render
from rest_framework import generics

from .models import Booking
from .serializers import BookingSerializer

# Create your views here.
# API 뷰
class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all();
    serializer_class = BookingSerializer

# API 뷰
class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer