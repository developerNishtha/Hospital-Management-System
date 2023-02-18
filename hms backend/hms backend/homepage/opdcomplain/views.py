from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import opdcomplainmodel

from homepage.models import homepagemodel

from django.http import HttpResponse ,HttpRequest
from django.contrib import messages
from opdcomplain.forms import Empforms
 

def showopdcomplain(request):
    showall=opdcomplainmodel.objects.all()
    return render(request,'show_opdcomplain.html',{"da":showall})

    

def Insertopdcomplain(request,UHIDid):
    print(UHIDid)
    getuhid=homepagemodel.objects.get(id=UHIDid)
    if request.method=="GET":
         return render(request,'opdcomplain.html',{'data':getuhid})
         
    if request.method=="POST":
        if request.POST.get('chiefcomplain') and request.POST.get('pastcomplain') and request.POST.get('followupvisit') and request.POST.get('opdcomplain_UHID_id') :

            todo=opdcomplainmodel()
            todo.chiefcomplain=request.POST.get('chiefcomplain')
            todo.pastcomplain=request.POST.get('pastcomplain')
            todo.followupvisit=request.POST.get('followupvisit')
            todo.opdcomplain_UHID_id=request.POST.get('opdcomplain_UHID_id')

            todo.save()
            messages.success(request,' data is saved successfully ..!')
            return render(request,'opdcomplain.html',{'data':getuhid})

    else:
        return render(request,'opdcomplain.html',{'data':getuhid})

def Editopdcomplain(request:HttpRequest,id):
    editempobj=opdcomplainmodel.objects.get(id=id)
    return render(request,'update_showopdcomplain.html',{"opdcomplainmodel":editempobj})

def updateopdcomplain(request:HttpRequest,id):
    Updateemp=opdcomplainmodel.objects.get(id=id)
    fo=Empforms(request.POST,instance=Updateemp)
    if fo.is_valid():
        fo.save()
        messages.success(request,'record updated successfully ..!')
        return render(request,'update_showopdcomplain.html',{"opdcomplainmodel":Updateemp})

   
    
def Delopdcomplain(request,id):
    delopdcomplain=opdcomplainmodel.objects.get(id=id)
    delopdcomplain.delete()
    showdata=opdcomplainmodel.objects.all()
    return render(request,'show_opdcomplain.html',{"data":showdata})
