from django.shortcuts import render
from main.models import Destinations
def home(request):
    return render(request,'home.html')

def explorer(request):
    destination=Destinations.objects.all()
    offer_rate=20.0
    return render(request,'mypages/Explore.html',{'destination':destination,'off':offer_rate})

def userProfile(request):
    return render(request,'mypages/userProfile.html')