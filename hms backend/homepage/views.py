from django.shortcuts import render,redirect
from .models import homepagemodel
from django.http import HttpResponse ,HttpRequest
from django.contrib import messages
from homepage.forms import Empforms

from .models import Newuser
from django.contrib.auth import logout

# def Index(request):
#     return render(request, 'a.html')

# def Usereg(request):
#     if request.method=="POST":
#         if request.POST.get('Username') and request.POST.get('Email') and request.POST.get('pwd'):
#             print("PARTH")
#             todo=Newuser()
#             todo.Username=request.POST.get('Username')
#             todo.Email=request.POST.get('Email')
#             todo.pwd=request.POST.get('pwd')

#             todo.save()
#             messages.success(request,' The New User '+request.POST['Username']+' is saved successfully ..!')
#             return render(request,'homepage.html')

#     else:
#         return render(request,'Registration.html')

# def loginpage(request):
#     if request.method=="POST":
#         try:
#             userdetails=Newuser.objects.get(Username=request.POST['Username'], pwd=request.POST['pwd'])
#             print("Username=",userdetails)
#             request.session['Username']=userdetails.Username
#             request.session['pwd']=userdetails.pwd
#             return render(request,'homepage.html')
#         except Newuser.DoesNotExist as e:
#             messages.success(request,'Username/ Password Invalid..!!')
    
#     return render(request,'Login.html')

# def logoutuser(request):
#     logout(request)
    
#     return render(request,'Login.html')

def showhomepage(request):
    showall=homepagemodel.objects.all()
    return render(request,'homepage.html',{"d":showall})

    

def Inserthomepage(request:HttpRequest):
    if request.method=="POST":
        if request.POST.get('uhid') and request.POST.get('registration_date') and request.POST.get('registration_time') and request.POST.get('aadhar_number') and request.POST.get('prefix') and request.POST.get('first_name') and request.POST.get('middle_name') and request.POST.get('last_name') and request.POST.get('birthday') and request.POST.get('gender') and request.POST.get('blood_group') and request.POST.get('marital_status') and request.POST.get('age') and request.POST.get('weight') and request.POST.get('height') and request.POST.get('occupation') and request.POST.get('email_id') and request.POST.get('contact_no') and request.POST.get('address_line_1') and request.POST.get('address_line_2') and request.POST.get('city') and request.POST.get('pincode') and request.POST.get('allerge_details')  :

            todo=homepagemodel()
            todo.uhid=request.POST.get('uhid')
            todo.registration_date=request.POST.get('registration_date')
            todo.registration_time=request.POST.get('registration_time')
            todo.aadhar_number=request.POST.get('aadhar_number')
            todo.prefix=request.POST.get('prefix')
            todo.first_name=request.POST.get('first_name')
            todo.middle_name=request.POST.get('middle_name')
            todo.last_name=request.POST.get('last_name')
            todo.birthday=request.POST.get('birthday')
            todo.gender=request.POST.get('gender')
            todo.blood_group=request.POST.get('blood_group')
            todo.marital_status=request.POST.get('marital_status')
            todo.age=request.POST.get('age')
            todo.weight=request.POST.get('weight')
            todo.height=request.POST.get('height')
            todo.occupation=request.POST.get('occupation')
            todo.email_id=request.POST.get('email_id')
            todo.contact_no=request.POST.get('contact_no')
            todo.address_line_1=request.POST.get('address_line_1')
            todo.address_line_2=request.POST.get('address_line_2')
            todo.city=request.POST.get('city')
            todo.pincode=request.POST.get('pincode')
            todo.allerge_details=request.POST.get('allerge_details')
            todo.save()
            messages.success(request,' data is saved successfully ..!')
            showhomepage(request)
            return render(request,'homepage.html')

    else:
        return render(request,'homepage.html')

def Edithomepage(request:HttpRequest,id):
    editempobj=homepagemodel.objects.get(id=id)
    return render(request,'update_homepage.html',{"homepagemodel":editempobj})

def updatehomepage(request:HttpRequest,id):
    Updateemp=homepagemodel.objects.get(id=id)
    fo=Empforms(request.POST,instance=Updateemp)
    if fo.is_valid():
        fo.save()
        messages.success(request,'record updated successfully ..!')
        return render(request,'update_homepage.html',{"homepagemodel":Updateemp})

   
    
def Delhomepage(request,id):
    delhomepage=homepagemodel.objects.get(id=id)
    delhomepage.delete()
    showdata=homepagemodel.objects.all()
    return render(request,'homepage.html',{"data":showdata})
