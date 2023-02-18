from django.shortcuts import render,redirect
from Loginsys.models import Newuser
from django.contrib import messages
from django.contrib.auth import logout

def Index(request):
    return render(request, 'Index.html')

def Usereg(request):
    if request.method=="POST":
        if request.POST.get('Username') and request.POST.get('Email') and request.POST.get('pwd'):
            print("PARTH")
            todo=Newuser()
            todo.Username=request.POST.get('Username')
            todo.Email=request.POST.get('Email')
            todo.pwd=request.POST.get('pwd')

            todo.save()
            messages.success(request,' The New User '+request.POST['Username']+' is saved successfully ..!')
            return render(request,'Index.html')

    else:
        return render(request,'Registration.html')

def loginpage(request):
    if request.method=="POST":
        try:
            userdetails=Newuser.objects.get(Username=request.POST['Username'], pwd=request.POST['pwd'])
            print("Username=",userdetails)
            request.session['Username']=userdetails.Username
            request.session['pwd']=userdetails.pwd
            return render(request,'Index.html')
            
        except Newuser.DoesNotExist as e:
            messages.success(request,'Username/ Password Invalid..!!')
    
    return render(request,'Login.html')

def logoutuser(request):
    # logout(request)
    try:
        del request.session['Username']
    except:
        return render(request,'Index.html')
    return render(request,'Index.html')
