from django.urls import path
from .consumers import FleetTrackConsumer,FleetTrackConsumer

websocket_urlpatterns=[
    path('ws/fleettracking/<str:truckid>/',FleetTrackConsumer.as_asgi()),
    path('ws/sendnotification/<str:fleetuser>/',FleetTrackConsumer.as_asgi()),
]