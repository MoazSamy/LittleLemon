from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from .serializers import bookingSerializer, UserSerializer
from .models import Booking

def index(request):
    return render(request, "index.html", {"message":"This is the static content."})
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]