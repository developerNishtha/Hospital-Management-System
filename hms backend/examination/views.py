from django.shortcuts import render,redirect
from .models import OPD_Examination
from homepage.models import homepagemodel
from django.http import HttpResponse ,HttpRequest
from django.contrib import messages
from examination.forms import Empforms
 

def showopd_examination(request):
    showall=OPD_Examination.objects.all()
    return render(request,'show_opd_examination.html',{"d":showall})

    

def Insertopd_examination(request,UHIDid):
    print(UHIDid)
    getuhid=homepagemodel.objects.get(id=UHIDid)
    if request.method=="GET":
         return render(request,'opd_examination.html',{'data':getuhid})
    if request.method=="POST":
        if request.POST.get('local_examination') and request.POST.get('dre') and request.POST.get('systematic_examination') and request.POST.get('UHID_id') :

            todo=OPD_Examination()
            todo.local_examination=request.POST.get('local_examination')
            todo.dre=request.POST.get('dre')
            todo.systematic_examination=request.POST.get('systematic_examination')
            todo.UHID_id=request.POST.get('UHID_id')
            
            todo.save()
            messages.success(request,' data is saved successfully ..!')
            return render(request,'opd_examination.html',{'data':getuhid})

    else:
        return render(request,'opd_examination.html',{'data':getuhid})
    
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

def Editopd_examination(request:HttpRequest,id):
    editempobj=OPD_Examination.objects.get(id=id)
    return render(request,'update_opd_examination.html',{"OPD_Examination":editempobj})

def updateempopddiagnosis(request:HttpRequest,id):
    # print(UHIDid)
    # getuhid=homepagemodel.objects.get(id=UHIDid)
    # if request.method=="GET":
    #      return render(request,'opd_examination.html',{'data':getuhid})
    Updateemp=OPD_Examination.objects.get(id=id)
    fo=Empforms(request.POST,instance=Updateemp)
    if fo.is_valid():
        fo.save()
        messages.success(request,'record updated successfully ..!')
        return render(request,'update_opd_examination.html',{"OPD_Examination":Updateemp})

   
    
def Delempopddiagnosis(request,id):
    deldiagnosis=OPD_Examination.objects.get(id=id)
    deldiagnosis.delete()
    showdata=OPD_Examination.objects.all()
    return render(request,'show_opd_examination.html',{"data":showdata})
