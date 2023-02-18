from django.shortcuts import render,redirect
from .models import ipd_registration
from django.http import HttpResponse ,HttpRequest
from django.contrib import messages
from ipd_registration.forms import Empforms
 

def showipd_registration(request):
    showall=ipd_registration.objects.all()
    return render(request,'ipd_registration.html',{"data":showall})

    

def Insertipd_registration(request:HttpRequest):
    if request.method=="POST":
        if request.POST.get('registration_time') and request.POST.get('registration_date') and request.POST.get('patient_category') :

            todo=ipd_registration()
            todo.registration_time=request.POST.get('registration_time')
            todo.registration_date=request.POST.get('registration_date')
            todo.patient_category=request.POST.get('patient_category')
            todo.save()
            messages.success(request,' data is saved successfully ..!')
            return render(request,'insert.html')

    else:
        return render(request,'insert.html')

def Editipd_registration(request:HttpRequest,id):
    editempobj=ipd_registration.objects.get(id=id)
    return render(request,'update.html',{"ipd_registration":editempobj})

def updateempipd_registration(request:HttpResponse,id):
    Updateemp=ipd_registration.objects.get(id=id)
    fo=Empforms(request.POST,instance=Updateemp)
    if fo.is_valid():
        fo.save()
        messages.success(request,'record updated successfully ..!')
        return render(request,'update.html',{"ipd_registration":Updateemp})

    
def Delempipd_registration(request,id):
    delipd_registration=ipd_registration.objects.get(id=id)
    delipd_registration.delete()
    showdata=ipd_registration.objects.all()
    return render(request,'ipd_registration.html',{"data":showdata})
