from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth  import get_user_model,authenticate,login,logout

# Create your views here.

User = get_user_model()

def login_view(request):
    
    if request.method=="POST":
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)

        if email and password:
            user =  authenticate(username=email,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,message="Invalid Credentials")
                return redirect('login')

        messages.error(request,message="empty form submitted")
        
    return render(request,'login.html')

def register(request):
    
    if request.method=="POST":
        
        name = request.POST.get('name',None)
        email = request.POST.get('email',None)
        phone = request.POST.get('phone',None)
        dob = request.POST.get('dob',None)
        password = request.POST.get('password',None)
        
        if (name and email and phone and dob and password):
            try:
                user = User.objects.create_user(name=name,email=email,password=password,phone=phone,dob=dob)
            
                if user:
                    user.set_password(password)
                    messages.success(request,message="User Created")
                    return redirect('login')
                    
            except:
                messages.error(request,message="user already exist")
                return redirect('login')
                
        else:
            # print(name,email,dob,phone,)
            messages.error(request,message="form not valid")
                
    
    return render(request,'register.html')


def logout_view(request):
    
    logout(request)
    return redirect('login')
