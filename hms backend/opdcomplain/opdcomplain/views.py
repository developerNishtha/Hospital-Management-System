from django.shortcuts import render,redirect
from .models import opdcomplainmodel
from django.http import HttpResponse ,HttpRequest
from django.contrib import messages
from opdcomplain.forms import Empforms
 

def showopdcomplain(request):
    showall=opdcomplainmodel.objects.all()
    return render(request,'opdcomplain.html',{"data":showall})

    

def Insertopdcomplain(request:HttpRequest):
    if request.method=="POST":
        if request.POST.get('chiefcomplain') and request.POST.get('pastcomplain') and request.POST.get('followupvisit') :

            todo=opdcomplainmodel()
            todo.chiefcomplain=request.POST.get('chiefcomplain')
            todo.pastcomplain=request.POST.get('pastcomplain')
            todo.followupvisit=request.POST.get('followupvisit')

            todo.save()
            messages.success(request,' data is saved successfully ..!')
            return render(request,'opdcomplain.html')

    else:
        return render(request,'opdcomplain.html')

def Editopdcomplain(request:HttpRequest,id):
    editempobj=opdcomplainmodel.objects.get(id=id)
    return render(request,'opdcomplain.html',{"opdcomplainmodel":editempobj})

def updateopdcomplain(request:HttpRequest,id):
    Updateemp=opdcomplainmodel.objects.get(id=id)
    fo=Empforms(request.POST,instance=Updateemp)
    if fo.is_valid():
        fo.save()
        messages.success(request,'record updated successfully ..!')
        return render(request,'opdcomplain.html',{"opdcomplainmodel":Updateemp})

   
    
def Delopdcomplain(request,id):
    delopdcomplain=opdcomplainmodel.objects.get(id=id)
    delopdcomplain.delete()
    showdata=opdcomplainmodel.objects.all()
    return render(request,'opdcomplain.html',{"data":showdata})
