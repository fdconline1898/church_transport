from django.contrib import admin
from django.urls import path, include
from transportation import views as t_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', t_views.coordinator_dashboard, name='coordinator_dashboard'),
    path('driver/', t_views.driver_route, name='driver_route'),
    path('request-ride/', t_views.rider_request, name='rider_request'),
    path('', include('transportation.urls')),
]
