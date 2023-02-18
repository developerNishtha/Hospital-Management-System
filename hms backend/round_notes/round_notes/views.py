from django.shortcuts import render,redirect
from .models import round_notesmodel
from django.http import HttpResponse ,HttpRequest
from django.contrib import messages
from round_notes.forms import Empforms
 

def showround_notes(request):
    showall=round_notesmodel.objects.all()
    return render(request,'round_notes.html',{"data":showall})

    

def Insertround_notes(request:HttpRequest):
    if request.method=="POST":
        print(request.method)
        if request.POST.get('round_note_number') and request.POST.get('rn_date') and  request.POST.get('rn_time') and request.POST.get('rmo_dr_name') and request.POST.get('dr_name') and request.POST.get('visit_type') and request.POST.get('symptons') and request.POST.get('examination') and request.POST.get('nursing_advise') and request.POST.get('lab_test_order') and request.POST.get('diagnostic_test_order') and request.POST.get('assessment') and request.POST.get('treatement_plan') and request.POST.get('blood_transfusion'):
            print("PARTH")
            todo=round_notesmodel()
            todo.round_note_number=request.POST.get('round_note_number')
            todo.rn_date=request.POST.get('rn_date')
            todo.rn_time=request.POST.get('rn_time')
            todo.rmo_dr_name=request.POST.get('rmo_dr_name')
            todo.dr_name=request.POST.get('dr_name')
            todo.visit_type=request.POST.get('visit_type')
            todo.symptons=request.POST.get('symptons')
            todo.examination=request.POST.get('examination')
            todo.nursing_advise=request.POST.get('nursing_advise')
            todo.lab_test_order=request.POST.get('lab_test_order')
            todo.diagnostic_test_order=request.POST.get('diagnostic_test_order')
            todo.assessment=request.POST.get('assessment')
            todo.treatement_plan=request.POST.get('treatement_plan')
            todo.blood_transfusion=request.POST.get('blood_transfusion')
            

            todo.save()
            messages.success(request,' data is saved successfully ..!')
            return render(request,'round_notes.html')
        
    else:
        return render(request,'round_notes.html')

def Editround_notes(request:HttpRequest,id):
    editempobj=round_notesmodel.objects.get(id=id)
    return render(request,'round_notes.html',{"round_notesmodel":editempobj})

def updateround_notes(request:HttpRequest,id):
    Updateemp=round_notesmodel.objects.get(id=id)
    fo=Empforms(request.POST,instance=Updateemp)
    if fo.is_valid():
        fo.save()
        messages.success(request,'record updated successfully ..!')
        return render(request,'round_notes.html',{"round_notesmodel":Updateemp})
    
def Delround_notes(request,id):
    delround_notes=round_notesmodel.objects.get(id=id)
    delround_notes.delete()
    showdata=round_notesmodel.objects.all()
    return render(request,'round_notes.html',{"data":showdata})
