
# Register your models here.
"""Markers admin."""

from django.contrib.gis import admin

from .models import Marker


@admin.register(Marker)
class MarkerAdmin(admin.OSMGeoAdmin):
    """Marker admin."""

    list_display = ("name", "location")