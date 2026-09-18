from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RiderViewSet, DriverViewSet, TripViewSet, TripRiderViewSet,
    coordinator_dashboard, driver_route, rider_request
)

router = DefaultRouter()
router.register(r'riders', RiderViewSet)
router.register(r'drivers', DriverViewSet)
router.register(r'trips', TripViewSet)
router.register(r'trip-riders', TripRiderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    # ⭐ Add your HTML pages here
    path('coordinator/', coordinator_dashboard, name='coordinator_dashboard'),
    path('driver/', driver_route, name='driver_route'),
    path('rider-request/', rider_request, name='rider_request'),
]
