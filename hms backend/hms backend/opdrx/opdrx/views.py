from django.shortcuts import render,redirect
from .models import opdrxmodel
from django.http import HttpResponse ,HttpRequest
from django.contrib import messages
from opdrx.forms import opdrxform
 

def showopdrx(request):
    showall=opdrxmodel.objects.all()
    return render(request,'opdrx.html',{"data":showall})

    

def Insertopdrx(request:HttpRequest):
    if request.method=="POST":
        if request.POST.get('medicinename') and request.POST.get('doctorname') and request.POST.get('dosage') and request.POST.get('route')  and request.POST.get('entreperiod') and request.POST.get('duration') and request.POST.get('total') and request.POST.get('followupinstruction') and request.POST.get('todaydate') and request.POST.get('todaytime') and request.POST.get('nextfollowupdate') and request.POST.get('nextfollowuptime')   :

            todo=opdrxmodel()
            todo.chiefcomplain=request.POST.get('medicinename')
            todo.pastcomplain=request.POST.get('doctorname')
            todo.followupvisit=request.POST.get('dosage')
            todo.followupvisit=request.POST.get('route') 
            todo.followupvisit=request.POST.get('entreperiod')
            todo.followupvisit=request.POST.get('duration')
            todo.followupvisit=request.POST.get('total')
            todo.followupvisit=request.POST.get('followupinstruction')  
            todo.followupvisit=request.POST.get('todaydate')   
            todo.followupvisit=request.POST.get('todaytime')  
            todo.followupvisit=request.POST.get('nextfollowupdate')  
            todo.followupvisit=request.POST.get('nextfollowuptime')  
            
            todo.save()
            messages.success(request,' data is saved successfully ..!')
            return render(request,'opdrx.html')

    else:
        return render(request,'opdrx.html')

# def Editopdcomplain(request:HttpRequest,id):
#     editempobj=opdcomplainmodel.objects.get(id=id)
#     return render(request,'opdcomplain.html',{"opdcomplainmodel":editempobj})

# def updateopdcomplain(request:HttpRequest,id):
#     Updateemp=opdcomplainmodel.objects.get(id=id)
#     fo=Empforms(request.POST,instance=Updateemp)
#     if fo.is_valid():
#         fo.save()
#         messages.success(request,'record updated successfully ..!')
#         return render(request,'opdcomplain.html',{"opdcomplainmodel":Updateemp})

   
    
# def Delopdcomplain(request,id):
#     delopdcomplain=opdcomplainmodel.objects.get(id=id)
#     delopdcomplain.delete()
#     showdata=opdcomplainmodel.objects.all()
#     return render(request,'opdcomplain.html',{"data":showdata})
