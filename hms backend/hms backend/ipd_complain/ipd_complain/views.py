from django.shortcuts import render,redirect
from .models import ipd_complainmodel
from django.http import HttpResponse ,HttpRequest
from django.contrib import messages
from ipd_complain.forms import Empforms
 

def showipd_complain(request):
    showall=ipd_complainmodel.objects.all()
    return render(request,'ipd_complain.html',{"data":showall})

    

def Insertipd_complain(request:HttpRequest):
    if request.method=="POST":
        if request.POST.get('chiefcomplain') and request.POST.get('pastcomplain') and request.POST.get('followupvisit') :

            todo=ipd_complainmodel()
            todo.chiefcomplain=request.POST.get('chiefcomplain')
            todo.pastcomplain=request.POST.get('pastcomplain')
            todo.followupvisit=request.POST.get('followupvisit')

            todo.save()
            messages.success(request,' data is saved successfully ..!')
            return render(request,'insert_ipd_complain.html')

    else:
        return render(request,'insert_ipd_complain.html')

def Editipd_complain(request:HttpRequest,id):
    editempobj=ipd_complainmodel.objects.get(id=id)
    return render(request,'update_ipd_complain.html',{"ipd_complainmodel":editempobj})

def updateipd_complain(request:HttpRequest,id):
    Updateemp=ipd_complainmodel.objects.get(id=id)
    fo=Empforms(request.POST,instance=Updateemp)
    if fo.is_valid():
        fo.save()
        messages.success(request,'record updated successfully ..!')
        return render(request,'update_ipd_complain.html',{"ipd_complainmodel":Updateemp})

   
    
def Delipd_complain(request,id):
    delipd_complain=ipd_complainmodel.objects.get(id=id)
    delipd_complain.delete()
    showdata=ipd_complainmodel.objects.all()
    return render(request,'ipd_complain.html',{"data":showdata})
