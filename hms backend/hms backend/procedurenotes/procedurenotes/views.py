from django.shortcuts import render,redirect
from .models import procedurenotesmodel
from django.http import HttpResponse ,HttpRequest
from django.contrib import messages
from procedurenotes.forms import Empforms
 

def showprocedurenotes(request):
    showall=procedurenotesmodel.objects.all()
    return render(request,'procedurenotes.html',{"data":showall})

    

def Insertprocedurenotes(request:HttpRequest):
    if request.method=="POST":
        
        if request.POST.get('procedure_date') and request.POST.get('procedure_name') and request.POST.get('ot_name') and request.POST.get('procedure_time') and request.POST.get('in_time') and request.POST.get('out_time') and request.POST.get('surgeon_name') and request.POST.get('assistant_surgeon_1') and request.POST.get('assistant_surgeon_2') and request.POST.get('anastheiologist') and request.POST.get('procedure_type') and request.POST.get('symoptom_of_infection') and request.POST.get('culture_report') and request.POST.get('operation_status') and request.POST.get('risk_factors') and request.POST.get('anasthesia_notes') and request.POST.get('pre_operative_notes') and request.POST.get('post_operative_notes') and request.POST.get('procedure_notes') and request.POST.get('remarks')  :
            
            todo=procedurenotesmodel()
            todo.procedure_date=request.POST.get('procedure_date')
            todo.procedure_name=request.POST.get('procedure_name')
            todo.ot_name=request.POST.get('ot_name')
            todo.procedure_time=request.POST.get('procedure_time')
            todo.in_time=request.POST.get('in_time')
            todo.out_time=request.POST.get('out_time')
            todo.surgeon_name=request.POST.get('surgeon_name')
            todo.assistant_surgeon_1=request.POST.get('assistant_surgeon_1')
            todo.assistant_surgeon_2=request.POST.get('assistant_surgeon_2')
            todo.anastheiologist=request.POST.get('anastheiologist')
            todo.procedure_type=request.POST.get('procedure_type')
            todo.symoptom_of_infection=request.POST.get('symoptom_of_infection')
            todo.culture_report=request.POST.get('culture_report')
            todo.operation_status=request.POST.get('operation_status')
            todo.risk_factors=request.POST.get('risk_factors')
            todo.anasthesia_notes=request.POST.get('anasthesia_notes')
            todo.pre_operative_notes=request.POST.get('pre_operative_notes')
            todo.post_operative_notes=request.POST.get('post_operative_notes')
            todo.procedure_notes=request.POST.get('procedure_notes')
            todo.remarks=request.POST.get('remarks')

            todo.save()
            messages.success(request,' data is saved successfully ..!')
            return render(request,'procedurenotes.html')

    else:
        return render(request,'procedurenotes.html')

def Editprocedurenotes(request:HttpRequest,id):
    editempobj=procedurenotesmodel.objects.get(id=id)
    return render(request,'procedurenotes.html',{"procedurenotesmodel":editempobj})

def updateprocedurenotes(request:HttpRequest,id):
    Updateemp=procedurenotesmodel.objects.get(id=id)
    fo=Empforms(request.POST,instance=Updateemp)
    if fo.is_valid():
        fo.save()
        messages.success(request,'record updated successfully ..!')
        return render(request,'procedurenotes.html',{"procedurenotesmodel":Updateemp})

   
    
def Delprocedurenotes(request,id):
    delprocedurenotes=procedurenotesmodel.objects.get(id=id)
    delprocedurenotes.delete()
    showdata=procedurenotesmodel.objects.all()
    return render(request,'procedurenotes.html',{"data":showdata})
