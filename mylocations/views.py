from operator import add
from django.shortcuts import render
"""Markers API views."""
from rest_framework import viewsets
from rest_framework_gis import filters

from django.http import HttpResponse

from .models import Marker
from .serializers import MarkerSerializer

import json

from django.contrib.gis.geos import GEOSGeometry


# Create your views here
def map(request):
    """A view to return the index page"""
    return render(request, "mylocations/map.html")


# Create your views here
def add_marker(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # A.geoCoords = GEOSGeometry('POINT(LON LAT)', srid=4326)
        location = {'name': data['name'], 'location': data['position'][0]}

        LAT = data['position'][0]['lat']
        LON = data['position'][0]['lng']

        try:
            add_location = Marker.objects.create(
                name=data['name'],
                location=GEOSGeometry(f'POINT({LON} {LAT})', srid=4326)
            )
        except Exception as e:
            print(e)        
        
    return render(request, "mylocations/add_marker.html")


class MarkerViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer
