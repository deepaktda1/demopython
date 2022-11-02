from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect('register')
    return render(request,'login1.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email = request.POST['email']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        password = request.POST['password']
        repassword = request.POST['password1']
        if password==repassword:
           if User.objects.filter(username=username).exists():
               messages.info(request,"username is exist")
               return redirect('register')
           elif User.objects.filter(email=email).exists():
               messages.info(request,'email is already exist')
               return redirect('register')
           else:
               user = User.objects.create_user ( username=username , email=email , first_name=firstname ,
                                                 last_name=lastname )
               user.save ()
               return redirect('login')
        else:
            messages.info(request,'password is not matched')
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')






