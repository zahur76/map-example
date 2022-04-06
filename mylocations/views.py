from django.shortcuts import render
"""Markers API views."""
from rest_framework import viewsets
from rest_framework_gis import filters

from .models import Marker
from .serializers import MarkerSerializer


# Create your views here
def map(request):
    """A view to return the index page"""
    return render(request, "mylocations/map.html")


class MarkerViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer
