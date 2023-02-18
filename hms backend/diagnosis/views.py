from django.shortcuts import render,redirect
from .models import Empmodel
from django.http import HttpResponse ,HttpRequest
from django.contrib import messages
from diagnosis.forms import Empforms

from homepage.models import homepagemodel
 

def showempdiagnosis(request):
    showall=Empmodel.objects.all()
    return render(request,'show_diagnosis.html',{"d":showall})

def showatnavbar(request,id):
    editt=Empmodel.objects.all()
    return render(request,'show_diagnosis.html',{"u":editt})


def Insertempdiagnosis(request:HttpRequest,UHIDid):
    print(UHIDid)
    getuhid=homepagemodel.objects.get(id=UHIDid)
    if request.method=="GET":
         return render(request,'opdcomplain.html',{'data':getuhid})

    if request.method=="POST":
        if request.POST.get('previousdiagnosis') and request.POST.get('finaldiagnosis') and request.POST.get('diagnosis_UHID_id'):

            todo=Empmodel()
            todo.previousdiagnosis=request.POST.get('previousdiagnosis')
            todo.finaldiagnosis=request.POST.get('finaldiagnosis')
            todo.diagnosis_UHID_id=request.POST.get('diagnosis_UHID_id')

            todo.save()
            messages.success(request,' data is saved successfully ..!')
            return render(request,'diagnosis.html')

    else:
        return render(request,'diagnosis.html')

# def Insertcoursedetails(request,courseid):
#     getcoursename=coursename.objects.get(id=courseid)
#     if request.method=="GET":
#         return render(request,'addcoursedetails.html',{'data':getcoursename})
#     elif request.method=="POST":
#         if request.POST.get('course_name') and request.POST.get('level') and request.POST.get('duration') and request.POST.get('fees') and request.POST.get('courses_id') :
#             todo=coursedetails()
#             todo.course_details=request.POST.get('course_name')
#             todo.level=request.POST.get('level')
#             todo.duration=request.POST.get('duration')
#             todo.fees=request.POST.get('fees')
#             todo.courses_id=request.POST.get('courses_id')
            
#             todo.save()
#             return render(request,'insert_coursename.html')

def Editempopddiagnosis(request:HttpRequest,id):
    editempobj=Empmodel.objects.get(id=id)
    return render(request,'update.html',{"Empmodel":editempobj})

def updateempopddiagnosis(request:HttpRequest,id):
    Updateemp=Empmodel.objects.get(id=id)
    fo=Empforms(request.POST,instance=Updateemp)
    if fo.is_valid():
        fo.save()
        messages.success(request,'record updated successfully ..!')
        return render(request,'update.html',{"Empmodel":Updateemp})

    
    
def Delempopddiagnosis(request,id):
    deldiagnosis=Empmodel.objects.get(id=id)
    deldiagnosis.delete()
    showdata=Empmodel.objects.all()
    return render(request,'diagnosis.html',{"data":showdata})
