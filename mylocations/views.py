from django.shortcuts import render

# Create your views here
def map(request):
    """A view to return the index page"""
    return render(request, "mylocations/map.html")