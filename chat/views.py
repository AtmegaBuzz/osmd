from django.shortcuts import render
from BookCab.models import CabGroup
from .consumers import WSConsumer

# Create your views here.
def chat(request,pk):
    
    group = CabGroup.objects.filter(id=pk)
    
    context = {
        'text':"hell",
        'group':group[0],
        'id':pk,
    }
    
    
    
    return render(request,'chat.html',context) 