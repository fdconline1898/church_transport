from django.shortcuts import render, redirect
from django.utils import timezone
from rest_framework import viewsets
from .models import Rider, Driver, Trip, TripRider
from .serializers import RiderSerializer, DriverSerializer, TripSerializer, TripRiderSerializer

class RiderViewSet(viewsets.ModelViewSet):
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class TripRiderViewSet(viewsets.ModelViewSet):
    queryset = TripRider.objects.all()
    serializer_class = TripRiderSerializer

def coordinator_dashboard(request):
    today = timezone.now().date()
    upcoming_trips = Trip.objects.filter(date__gte=today)
    unassigned_riders = Rider.objects.filter(active=True, recurring_weekly=True)
    return render(request, 'transportation/coordinator_dashboard.html', {
        'upcoming_trips': upcoming_trips,
        'unassigned_riders': unassigned_riders
    })

def driver_route(request):
    today = timezone.now().date()
    trips_today = Trip.objects.filter(date=today)
    return render(request, 'transportation/driver_route.html', {
        'trips_today': trips_today
    })

def rider_request(request):
    if request.method == 'POST':
        Rider.objects.create(
            full_name=request.POST['full_name'],
            phone=request.POST['phone'],
            address_line1=request.POST['address_line1'],
            city=request.POST['city'],
            state=request.POST['state'],
            zip_code=request.POST['zip_code'],
            preferred_service_time=request.POST['preferred_service_time'],
            recurring_weekly=('recurring_weekly' in request.POST)
        )
        return redirect('coordinator_dashboard')
    return render(request, 'transportation/rider_request.html')
