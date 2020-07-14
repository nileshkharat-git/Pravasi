from django.shortcuts import render,redirect
from .models import customer
from django.contrib.messages import error,success
from main.models import accounts
from .forms import updateProfile
from main.models import Destinations
from django.contrib.auth.decorators import login_required



@login_required(login_url='/user/login/')
def myprofile(request,email):
    """"this function invoke customer object and send it to userprofile.html"""
    cust=customer.objects.filter(email=email)
    form=updateProfile(request.POST or None,request.FILES or None,instance=accounts.objects.get(email=email))
    if form.is_valid():
        form.save()
        success(request,"Profile has been updated.")
        return redirect(myprofile,email)
    return render(request,'mypages/userProfile.html',{'cust':cust,'form':form})


@login_required(login_url='/user/login/')
def booking(request):
    if request.POST:
        email=request.POST['email']
        rate=float(request.POST['rot'])
        nop=float(request.POST['nop'])
        doj=request.POST['doj']
        place=request.POST['place']
        total=rate*nop
        noPassenger=nop

        instance=accounts.objects.get(email=email)
        user=customer(email=instance,place=place,noPassenger=noPassenger,total=total,DOJ=doj)
        user.save()

        return redirect(myprofile,request.POST['email'])

    book_entry=Destinations.objects.get(Place=request.GET['place'])
    if(book_entry.inOffer):
        book_entry.RateOfTicket=book_entry.RateOfTicket-((book_entry.RateOfTicket/100)*20)

    return render(request,'mypages/booking.html',{'book':book_entry})

