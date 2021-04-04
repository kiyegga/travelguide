from django.shortcuts import render
from .models import Destination, Packages

# Create your views here.
def index(request):
    packs = Packages.objects.all()
    dest = Destination.objects.all()
    
    # baseUrl
    context = {
         'dest' : dest, 
         'packs' : packs
    }
    return render(request, 'index.html', context)
  