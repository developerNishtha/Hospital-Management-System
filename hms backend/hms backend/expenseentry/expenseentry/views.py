from django.shortcuts import render,redirect
from .models import expenseentrymodel
from django.http import HttpResponse ,HttpRequest
from django.contrib import messages
from expenseentry.forms import Empforms
 

def showexpenseentry(request):
    showall=expenseentrymodel.objects.all()
    return render(request,'expenseentry.html',{"data":showall})

    

def Insertexpenseentry(request:HttpRequest):
    if request.method=="POST":
        if request.POST.get('preparedby') and request.POST.get('remarks') and request.POST.get('expenseamount') and request.POST.get('expensetype') and request.POST.get('expensename') and request.POST.get('entrycode'):
        
            todo=expenseentrymodel()
            todo.entrycode=request.POST.get('entrycode')
            todo.expensename=request.POST.get('expensename')
            todo.expensetype=request.POST.get('expensetype')
            todo.preparedby=request.POST.get('preparedby')
            todo.remarks=request.POST.get('remarks')
            todo.expenseamount=request.POST.get('expenseamount')
            
            todo.save()
            messages.success(request,' data is saved successfully ..!')
            return render(request,'expenseentry.html')

    else:
        return render(request,'expenseentry.html')

def Editexpenseentry(request:HttpRequest,id):
    editexpenseentry=expenseentrymodel.objects.get(id=id)
    return render(request,'expenseentry.html',{"expenseentrymodel":editexpenseentry})

def updateexpenseentry(request:HttpRequest,id):
    Updateexpenseentry=expenseentrymodel.objects.get(id=id)
    fo=Empforms(request.POST,instance=Updateexpenseentry)
    if fo.is_valid():
        fo.save()
        messages.success(request,'record updated successfully ..!')
        return render(request,'expenseentry.html',{"expenseentrymodel":Updateexpenseentry})

   
    
def Delexpenseentry(request,id):
    deleexpenseentry=expenseentrymodel.objects.get(id=id)
    deleexpenseentry.delete()
    showdata=expenseentrymodel.objects.all()
    return render(request,'expenseentry.html',{"data":showdata})
