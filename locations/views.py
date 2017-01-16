from django.shortcuts import render
from .models import Location

def index(request):
    locations_list = Location.objects.all()
    return render(request, 'locations/index.html', {'locations': locations_list,})


