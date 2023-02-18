from django.shortcuts import render,redirect
from .models import opdrxmodel
from django.http import HttpResponse ,HttpRequest
from django.contrib import messages
from opdrx.forms import Empforms
 

def showopdrx(request):
    showall=opdrxmodel.objects.all()
    return render(request,'opdrx.html',{"data":showall})

    

def Insertopdrx(request:HttpRequest):
    if request.method=="POST":
        print(request.method)
        if request.POST.get('medicinename') and request.POST.get('doctorname') and request.POST.get('dosage') and request.POST.get('route') and request.POST.get('entreperiod') and request.POST.get('entreperiod') and request.POST.get('duration') and request.POST.get('total') and request.POST.get('followupinstruction') and request.POST.get('todaydate') and request.POST.get('todaytime') and request.POST.get('nextfollowupdate') and request.POST.get('nextfollowuptime') :
            print("PARTH")
            todo=opdrxmodel()
            todo.medicinename=request.POST.get('medicinename')
            todo.doctorname=request.POST.get('doctorname')
            todo.dosage=request.POST.get('dosage')
            todo.route=request.POST.get('route') 
            todo.entreperiod=request.POST.get('entreperiod')
            todo.duration=request.POST.get('duration')
            todo.total=request.POST.get('total')
            todo.followupinstruction=request.POST.get('followupinstruction')  
            todo.todaydate=request.POST.get('todaydate')   
            todo.todaytime=request.POST.get('todaytime')  
            todo.nextfollowupdate=request.POST.get('nextfollowupdate')  
            todo.nextfollowuptime=request.POST.get('nextfollowuptime')  
            
            
            todo.save()
            messages.success(request,' data is saved successfully ..!')
            return render(request,'opdrx.html')

    else:
        return render(request,'opdrx.html')


def Editopdrx(request:HttpRequest,id):
    
    editempobj=opdrxmodel.objects.get(id=id)
    return render(request,'opdrx.html',{"opdrxmodel":editempobj})

def updateopdrx(request:HttpRequest,id):
    Updateemp=opdrxmodel.objects.get(id=id)
    fo=Empforms(request.POST,instance=Updateemp)
    if fo.is_valid():
        fo.save()
        messages.success(request,'record updated successfully ..!')
        return render(request,'opdrx.html',{"opdrxmodel":Updateemp})
   
    
# def Delopdcomplain(request,id):
#     delopdcomplain=opdcomplainmodel.objects.get(id=id)
#     delopdcomplain.delete()
#     showdata=opdcomplainmodel.objects.all()
#     return render(request,'opdcomplain.html',{"data":showdata})
