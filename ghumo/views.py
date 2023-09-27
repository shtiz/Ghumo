from django.shortcuts import render

from ghumo.models import Destination

# Create your views here.

def index(request):
    
    dests = Destination.objects.all
  
    return render(request , 'index.html' , {'dests' : dests})
