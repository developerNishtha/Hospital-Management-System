from django.shortcuts import render,redirect
from .models import OPD_Examination
from django.http import HttpResponse ,HttpRequest
from django.contrib import messages
from examination.forms import Empforms
 

def showopd_examination(request):
    showall=OPD_Examination.objects.all()
    return render(request,'opd_examination.html',{"data":showall})

    

def Insertopd_examination(request:HttpRequest):
    if request.method=="POST":
        if request.POST.get('local_examination') and request.POST.get('dre') and request.POST.get('systematic_examination') :

            todo=OPD_Examination()
            todo.local_examination=request.POST.get('local_examination')
            todo.dre=request.POST.get('dre')
            todo.systematic_examination=request.POST.get('systematic_examination')
            
            todo.save()
            messages.success(request,' data is saved successfully ..!')
            return render(request,'opd_examination.html')

    else:
        return render(request,'opd_examination.html')

def Editopd_examination(request:HttpRequest,id):
    editempobj=OPD_Examination.objects.get(id=id)
    return render(request,'opd_examination.html',{"OPD_Examination":editempobj})

def updateempopddiagnosis(request:HttpRequest,id):
    Updateemp=OPD_Examination.objects.get(id=id)
    fo=Empforms(request.POST,instance=Updateemp)
    if fo.is_valid():
        fo.save()
        messages.success(request,'record updated successfully ..!')
        return render(request,'opd_examination.html',{"OPD_Examination":Updateemp})

   
    
# def Delempopddiagnosis(request,id):
#     deldiagnosis=OPD_Examination.objects.get(id=id)
#     deldiagnosis.delete()
#     showdata=OPD_Examination.objects.all()
#     return render(request,'diagnosis.html',{"data":showdata})
