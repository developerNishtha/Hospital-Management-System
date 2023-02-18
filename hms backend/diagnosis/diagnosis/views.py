from django.shortcuts import render,redirect
from .models import Empmodel

from django.http import HttpResponse ,HttpRequest
from django.contrib import messages
from diagnosis.forms import Empforms
 

def showempdiagnosis(request):
    showall=Empmodel.objects.all()
    return render(request,'diagnosis.html',{"d":showall})

    

def Insertempdiagnosis(request:HttpRequest):
    if request.method=="POST":
        if request.POST.get('previousdiagnosis') and request.POST.get('finaldiagnosis') :

            todo=Empmodel()
            todo.previousdiagnosis=request.POST.get('previousdiagnosis')
            todo.finaldiagnosis=request.POST.get('finaldiagnosis')
            
            todo.save()
            messages.success(request,' data is saved successfully ..!')
            return render(request,'insert.html')

    else:
        return render(request,'insert.html')

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
