from re import M
from django.urls import path
from . import views

from .views import MarkerViewSet

urlpatterns = [
    path("", views.map, name="map"),
    path("add_marker", views.add_marker, name="add_marker"),
    path("markers", MarkerViewSet.as_view({'get': 'list'}), name="markers"),
]
