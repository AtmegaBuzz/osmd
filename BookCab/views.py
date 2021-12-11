from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from osmd.decorators import check_authentication
from .models import Booking, CabGroup
from django.contrib import messages
from osmd.algorithm import _main_
import random
# Create your views here.

source = "maharashtra"

@check_authentication
def home(request):
    
    if request.method=="POST":
        destination = request.POST.get("destination",None)
        
        try:
            # booking having status code ongoing
            bookings_ongoing = Booking.objects.all().filter(status=0)
            b = Booking.objects.create(destination=destination,user=request.user)
            if len(bookings_ongoing)>=4:
                print(bookings_ongoing)
                groups =  _main_()
                print(len(groups),"-----------")
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
                        print(usrAttr.booking_id,booking_a[0].destination,booking_a[0].status)
                           
                    
                    print("cab ended")
            else:
                print("added to ongoing queue")
            messages.success(request,message="request added successfuly")
            
                
        except Exception as e:
            messages.success(request,message="allocation failed try again later!")
            print("failed",e)

    return render(request,'index.html')

@check_authentication
def services(request):
    
    bookings = Booking.objects.all().filter(user=request.user)
    
    context = {
        "bookings":bookings,
    }
    
    return render(request,'index-3.html',context)

@check_authentication
def contact(request):
    return render(request,'index-4.html')

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
    
    
    

@check_authentication
def groupChat_view(request,pk):
    return HttpResponse("hello world",pk)