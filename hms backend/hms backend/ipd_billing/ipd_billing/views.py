from django.shortcuts import render,redirect
from .models import ipd_billingmodel
from django.http import HttpResponse ,HttpRequest
from django.contrib import messages
from ipd_billing.forms import Empforms
 

def showipd_billing(request):
    showall=ipd_billingmodel.objects.all()
    return render(request,'ipd_billing.html',{"data":showall})

    

def Insertipd_billing(request:HttpRequest):
    if request.method=="POST":
        if request.POST.get('uhid') and request.POST.get('dr_name') and request.POST.get('reffered_by') and request.POST.get('bill_code') and request.POST.get('bill_date') and request.POST.get('bill_time') and request.POST.get('caste_type') and request.POST.get('charge_price_list') and request.POST.get('charge_group') and request.POST.get('charge_code') and request.POST.get('charge_name') and request.POST.get('quantity_or_duration') and request.POST.get('rate') and request.POST.get('discount_in_percentage') and request.POST.get('discount_amount') and request.POST.get('net_amount')  :

            todo=ipd_billingmodel()
            todo.uhid=request.POST.get('uhid')
            todo.dr_name=request.POST.get('dr_name')
            todo.reffered_by=request.POST.get('reffered_by')
            todo.bill_code=request.POST.get('bill_code')
            todo.bill_date=request.POST.get('bill_date')
            todo.bill_time=request.POST.get('bill_time')
            todo.caste_type=request.POST.get('caste_type')
            todo.charge_price_list=request.POST.get('charge_price_list')
            todo.charge_group=request.POST.get('charge_group')
            todo.charge_code=request.POST.get('charge_code')
            todo.charge_name=request.POST.get('charge_name')
            todo.quantity_or_duration=request.POST.get('quantity_or_duration')
            todo.rate=request.POST.get('rate')
            todo.discount_in_percentage=request.POST.get('discount_in_percentage')
            todo.discount_amount=request.POST.get('discount_amount')
            todo.net_amount=request.POST.get('net_amount')

            todo.save()
            messages.success(request,' data is saved successfully ..!')
            return render(request,'ipd_billing.html')

    else:
        return render(request,'ipd_billing.html')

def Editipd_billing(request:HttpRequest,id):
    editempobj=ipd_billingmodel.objects.get(id=id)
    return render(request,'ipd_billing.html',{"ipd_billingmodel":editempobj})

def updateipd_billing(request:HttpRequest,id):
    Updateemp=ipd_billingmodel.objects.get(id=id)
    fo=Empforms(request.POST,instance=Updateemp)
    if fo.is_valid():
        fo.save()
        messages.success(request,'record updated successfully ..!')
        return render(request,'ipd_billing.html',{"ipd_billingmodel":Updateemp})

   
    
def Delipd_billing(request,id):
    delipd_billing=ipd_billingmodel.objects.get(id=id)
    delipd_billing.delete()
    showdata=ipd_billingmodel.objects.all()
    return render(request,'ipd_billing.html',{"data":showdata})
