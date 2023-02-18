from django.shortcuts import render,redirect
from .models import opd_pfsh
from django.http import HttpResponse ,HttpRequest
from django.contrib import messages
from opd_pfsh.forms import Empforms
 

def showopd_pfsh(request):
    showall=opd_pfsh.objects.all()
    return render(request,'opd_pfsh.html',{"data":showall})

    

def Insertopd_pfsh(request:HttpRequest):
    if request.method=="POST":
        if request.POST.get('previous_medical_history') and request.POST.get('family_medical_history') :

            todo=opd_pfsh()
            todo.previous_medical_history=request.POST.get('previous_medical_history')
            todo.family_medical_history=request.POST.get('family_medical_history')
            
            
            todo.save()
            messages.success(request,' data is saved successfully ..!')
            return render(request,'opd_pfsh.html')

    else:
        return render(request,'opd_pfsh.html')

def Editopd_pfsh(request:HttpRequest,id):
    editempobj=opd_pfsh.objects.get(id=id)
    return render(request,'opd_pfsh.html',{"opd_pfsh":editempobj})

# def updateempopd_pfsh(request:HttpRequest,id):
#     Updateemp=opd_pfsh.objects.get(id=id)
#     fo=Empforms(request.POST,instance=Updateemp)
#     if fo.is_valid():
#         fo.save()
#         messages.success(request,'record updated successfully ..!')
#         return render(request,'opd_pfsh.html',{"opd_pfsh":Updateemp})

   
    
def Delempopd_pfsh(request,id):
    delopd_pfsh=opd_pfsh.objects.get(id=id)
    delopd_pfsh.delete()
    showdata=opd_pfsh.objects.all()
    return render(request,'opd_pfsh.html',{"data":showdata})
