from django.urls import path
# from drf_yasg.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path("booking/", BookingList.as_view()),
    path("booking/<int:pk>/", BookingDetail.as_view()),
]