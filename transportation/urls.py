from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RiderViewSet, DriverViewSet, TripViewSet, TripRiderViewSet

router = DefaultRouter()
router.register(r'riders', RiderViewSet)
router.register(r'drivers', DriverViewSet)
router.register(r'trips', TripViewSet)
router.register(r'trip-riders', TripRiderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
