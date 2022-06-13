import random

from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.contrib import messages

from osmd.decorators import check_authentication
from osmd.algorithm import main

from BookCab.models import (
    Booking, 
    CabGroup,
    Source
)
# Create your views here.

# location of root organization offering the services

source = Source.objects.values_list(
    "location_name"
    ).all().first()

# set default root location
if not source:
    source = 'rajiv chowk'


@check_authentication
def home(request):
    
    if request.method=="POST":
        destination = request.POST.get("destination",None)
        
        try:
            # booking having status code ongoing
            bookings_ongoing = Booking.objects.all().filter(status=0)

            # create bookings if there are more than 4 ongoing request in queue
            Booking.objects.create(destination=destination,user=request.user)
            if bookings_ongoing.__len__()>=4:

                groups =  main()

                for group in groups:
                    name = f"grp{random.randint(1,10000)}:{random.randbytes(10000)}"
                    grp = CabGroup.objects.create(name=name)
                    for usrAttr in group:
                    
                        booking_a = Booking.objects.filter(id=usrAttr.booking_id)
                        booking_a.update(
                            status = 1,
                            group = grp.id,
                            cost = usrAttr.cost,
                            distance = usrAttr.distance,
                        )
                           
                    
            else:
                messages.success(request,message="request added successfuly")
            
                
        except Exception as e:
            messages.success(request,message="allocation failed try again later!")

    return render(request,'index.html')

@check_authentication
def services(request):
    
    bookings = Booking.objects.all().filter(user=request.user)
    
    context = {
        "bookings":bookings,
    }
    
    return render(request,'services.html',context)

@check_authentication
def contact(request):
    return render(request,'contact.html')

@check_authentication
def detailGroup_view(request,pk):
    
    group = CabGroup.objects.all().filter(id=pk)
    
    if group:
        grp_bookings = Booking.objects.all().filter(group=group[0])
        
        context = {
            "grp_bookings":grp_bookings,
            "group_id":pk,
        }
        
        return render(request,'detail_group.html',context) 
        
    else:
        raise Http404("No groups found")
    

