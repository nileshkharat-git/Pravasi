from django.shortcuts import render
from main.models import Destinations
def home(request):
    return render(request,'home.html')

def explorer(request):
    destination=Destinations.objects.all()
    return render(request,'mypages/Explore.html',{'destination':destination})

def userProfile(request):
    return render(request,'mypages/userProfile.html')