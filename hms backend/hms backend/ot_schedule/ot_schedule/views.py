from django.shortcuts import render,redirect
from .models import ot_schedulemodel
from django.http import HttpResponse ,HttpRequest
from django.contrib import messages
#from ot_schedule.forms import Empforms
 

def showot_schedule(request):
    showall=ot_schedulemodel.objects.all()
    return render(request,'ot_schedule.html',{"data":showall})

    

def Insertot_schedule(request:HttpRequest):
    if request.method=="POST":
        if request.POST.get('schedule_date') and request.POST.get('surgery_date') and request.POST.get('surgeon_name') and request.POST.get('surgery_start_time') and request.POST.get('surgery_end_time') and request.POST.get('ot_booked_by') and request.POST.get('schedule_status') and request.POST.get('procedure_name') and request.POST.get('notes') and request.POST.get('assistant1') and request.POST.get('assistant2') and request.POST.get('remarks') and request.POST.get('type_of_anasthesia') and request.POST.get('anastheiologist') and request.POST.get('requirements')  :

            todo=ot_schedulemodel()
            todo.schedule_date=request.POST.get('schedule_date')
            todo.surgery_date=request.POST.get('surgery_date')
            todo.surgeon_name=request.POST.get('surgeon_name')
            todo.surgery_start_time=request.POST.get('surgery_start_time')
            todo.surgery_end_time=request.POST.get('surgery_end_time')
            todo.ot_booked_by=request.POST.get('ot_booked_by')
            todo.schedule_status=request.POST.get('schedule_status')
            todo.procedure_name=request.POST.get('procedure_name')
            todo.notes=request.POST.get('notes')
            todo.assistant1=request.POST.get('assistant1')
            todo.assistant2=request.POST.get('assistant2')
            todo.remarks=request.POST.get('remarks')
            todo.type_of_anasthesia=request.POST.get('type_of_anasthesia')
            todo.anastheiologist=request.POST.get('anastheiologist')
            todo.requirements=request.POST.get('requirements')

            todo.save()
            messages.success(request,' data is saved successfully ..!')
            return render(request,'ot_schedule.html')

    else:
        return render(request,'ot_schedule.html')

# def Editot_schedule(request:HttpRequest,id):
#     editempobj=ot_schedulemodel.objects.get(id=id)
#     return render(request,'ot_schedule.html',{"ot_schedulemodel":editempobj})

# def updateot_schedule(request:HttpRequest,id):
#     Updateemp=ot_schedulemodel.objects.get(id=id)
#     fo=Empforms(request.POST,instance=Updateemp)
#     if fo.is_valid():
#         fo.save()
#         messages.success(request,'record updated successfully ..!')
#         return render(request,'ot_schedule.html',{"ot_schedulemodel":Updateemp})

   
    
def Delot_schedule(request,id):
    delot_schedule=ot_schedulemodel.objects.get(id=id)
    delot_schedule.delete()
    showdata=ot_schedulemodel.objects.all()
    return render(request,'ot_schedule.html',{"data":showdata})
