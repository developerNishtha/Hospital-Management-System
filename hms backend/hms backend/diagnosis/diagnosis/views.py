from django.shortcuts import render,redirect
from .models import Empmodel
from diagnosis.models import diagnosismodel
from django.http import HttpResponse ,HttpRequest
from django.contrib import messages
from diagnosis.forms import Empforms
 

def showempdiagnosis(request):
    showall=Empmodel.objects.all()
    return render(request,'show_diagnosis.html',{"data":showall})

    

def Insertempdiagnosis(request:HttpRequest):
    print()
    getuhid=diagnosismodel.objects.get()
    if request.method=="POST":
        if request.POST.get('previousdiagnosis') and request.POST.get('finaldiagnosis') :

            todo=Empmodel()
            todo.previousdiagnosis=request.POST.get('previousdiagnosis')
            todo.finaldiagnosis=request.POST.get('finaldiagnosis')
            
            todo.save()
            messages.success(request,' data is saved successfully ..!')
            return render(request,'diagnosis.html')

    else:
        return render(request,'diagnosis.html')

def Editempopddiagnosis(request:HttpRequest,id):
    editempobj=Empmodel.objects.get(id=id)
    return render(request,'diagnosis.html',{"Empmodel":editempobj})

def updateempopddiagnosis(request:HttpRequest,id):
    Updateemp=Empmodel.objects.get(id=id)
    fo=Empforms(request.POST,instance=Updateemp)
    if fo.is_valid():
        fo.save()
        messages.success(request,'record updated successfully ..!')
        return render(request,'diagnosis.html',{"Empmodel":Updateemp})

   
    
def Delempopddiagnosis(request,id):
    deldiagnosis=Empmodel.objects.get(id=id)
    deldiagnosis.delete()
    showdata=Empmodel.objects.all()
    return render(request,'diagnosis.html',{"data":showdata})
