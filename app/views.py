
from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
def  index(request):
    return render(request,'index.html')
def handlelogin(request):
     if request.method=="POST":
        uname=request.POST.get("username")
        pass1=request.POST.get("pass1")
        myuser=authenticate(username=uname,password=pass1)
        if myuser is not None:
           login(request,myuser)
           messages.success(request,"Login Success")
           return redirect('/')
        else:
           messages.error(request,"Invalid Credentials")
           return redirect('/login')
     return render(request,'login.html')


def handlesignup(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('pass1')
        confirmpassword=request.POST.get('pass2')
        #print(uname,email,password,confirmpassword)
        if password!=confirmpassword:
           messages.warning(request,"Password is Incorrect")
           return redirect('/signup')
         
          
        try:
           if User.objects.get(username=uname):
                messages.info(request,'UserName is Taken')
                return redirect('/signup')
        except:
           pass
        try:
           if User.objects.get(email=email):
                messages.info(request,'Email is Taken')
                return redirect('/signup')
        except:
           pass

        myuser=User.objects.create_user(uname,email,password)
        myuser.save()
        messages.success(request,'Signup Successful.Please Log In')
        return redirect('/login')
       
    

    return render(request,'signup.html')
 
