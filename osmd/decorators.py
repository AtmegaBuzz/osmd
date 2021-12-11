# decorators 
from django.shortcuts import redirect


def check_authentication(view_func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        else:
            return view_func(request,*args,**kwargs)
    
    return wrapper