from django.urls import path
from .views import *

urlpatterns = [
    path("booking/", BookingList.as_view()),
    path("booking/<int:pk>/", BookingDetail.as_view()),
]