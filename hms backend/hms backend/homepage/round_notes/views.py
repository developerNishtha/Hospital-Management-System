from django.shortcuts import render,redirect
from .models import round_notes
from homepage.models import homepagemodel
from django.http import HttpResponse ,HttpRequest
from django.contrib import messages
from round_notes.forms import Empforms
 

def showround_notes(request):
    showall=round_notes.objects.all()
    return render(request,'show_round_notes.html',{"d":showall})

    

def Insertround_notes(request,UHIDid):
    print(UHIDid)
    getuhid=homepagemodel.objects.get(id=UHIDid)
    if request.method=="GET":
         return render(request,'round_notes.html',{'data':getuhid})
    if request.method=="POST":
        if request.POST.get('round_note_number') and request.POST.get('date_rn') and request.POST.get('time_rn') and request.POST.get('rmo_dr_name') and request.POST.get('dr_name') and request.POST.get('visit_type') and request.POST.get('symptoms') and request.POST.get('examination') and request.POST.get('nursing_advice') and request.POST.get('lab_test_order') and request.POST.get('diagnostic_test_order') and request.POST.get('assessment') and request.POST.get('treatement_plan') and request.POST.get('blood_transfusion')  :

            todo=round_notes()
            todo.round_note_number=request.POST.get('round_note_number')
            todo.date_rn=request.POST.get('date_')
            todo.time_rn=request.POST.get('time_')
            todo.rmo_dr_name=request.POST.get('rmo_dr_name')
            todo.dr_name=request.POST.get('dr_name')
            todo.visit_type=request.POST.get('visit_type')
            todo.symptoms=request.POST.get('symptoms')
            todo.examination=request.POST.get('examination')
            todo.nursing_advice=request.POST.get('nursing_advice')
            todo.lab_test_order=request.POST.get('lab_test_order')
            todo.diagnostic_test_order=request.POST.get('diagnostic_test_order')
            todo.assessment=request.POST.get('assessment')
            todo.treatement_plan=request.POST.get('treatement_plan')
            todo.blood_transfusion=request.POST.get('blood_transfusion')
            todo.UHID_id=request.POST.get('UHID_id')
            
            todo.save()
            messages.success(request,' data is saved successfully ..!')
            return render(request,'round_notes.html',{'data':getuhid})

    else:
        return render(request,'round_notes.html',{'data':getuhid})
    

def Editround_notes(request:HttpRequest,id):
    editempobj=round_notes.objects.get(id=id)
    return render(request,'update_round_notes.html',{"round_notes":editempobj})

def updateempround_notes(request:HttpRequest,id):
    # print(UHIDid)
    # getuhid=homepagemodel.objects.get(id=UHIDid)
    # if request.method=="GET":
    #      return render(request,'round_notes.html',{'data':getuhid})
    Updateemp=round_notes.objects.get(id=id)
    fo=Empforms(request.POST,instance=Updateemp)
    if fo.is_valid():
        fo.save()
        messages.success(request,'record updated successfully ..!')
        return render(request,'update_round_notes.html',{"round_notes":Updateemp})

   
    
def Delempround_notes(request,id):
    delround_notes=round_notes.objects.get(id=id)
    delround_notes.delete()
    showdata=round_notes.objects.all()
    return render(request,'show_round_notes.html',{"data":showdata})
