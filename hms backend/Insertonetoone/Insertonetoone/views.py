from django.shortcuts import render,redirect
from .models import coursename ,coursedetails   
from django.http import HttpResponse ,HttpRequest
from django.contrib import messages

def showcoursename(request):
    showall=coursename.objects.all()
    return render(request,'insert_coursename.html',{"data":showall})

def Insertcoursename(request:HttpRequest):
    if request.method=="POST":
        print(request.method)
        if request.POST.get('cname') :
            print("PARTH")
            todo=coursename()
            todo.cname=request.POST.get('cname')
            
            todo.save()
            messages.success(request,' data is saved successfully ..!')
            return render(request,'insert_coursename.html')

    else:
        return render(request,'insert_coursename.html')

def Insertcoursedetails(request,courseid):
    getcoursename=coursename.objects.get(id=courseid)
    if request.method=="GET":
        return render(request,'addcoursedetails.html',{'data':getcoursename})
    elif request.method=="POST":
        if request.POST.get('course_name') and request.POST.get('level') and request.POST.get('duration') and request.POST.get('fees') and request.POST.get('courses_id') :
            todo=coursedetails()
            todo.course_details=request.POST.get('course_name')
            todo.level=request.POST.get('level')
            todo.duration=request.POST.get('duration')
            todo.fees=request.POST.get('fees')
            todo.courses_id=request.POST.get('courses_id')
            
            todo.save()
            return render(request,'insert_coursename.html')