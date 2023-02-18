from django.shortcuts import render, redirect
from .models import registration
from django.http import HttpResponse, HttpRequest
from django.contrib import messages


def showregistration(request):
    showall = registration.objects.all()
    return render(request, 'registration.html', {"data": showall})


def Insertregistration(request: HttpRequest):
    if request.method == "POST":
        if request.POST.get('firstname') and request.POST.get('firstname') and request.POST.get('middlename') and request.POST.get('lastname') and request.POST.get('adhaarcardnumber') and request.POST.get('gender') and request.POST.get('bloodgroup') and request.POST.get('birthdate') and request.POST.get('maritalstatus') and request.POST.get('occupation') and request.POST.get('registrationdate') and request.POST.get('registrationtime') and request.POST.get('age') and request.POST.get('weight') and request.POST.get('height') and request.POST.get('phonenumber') and request.POST.get('address1') and request.POST.get('address2') and request.POST.get('city') and request.POST.get('pincode') and request.POST.get('allergydetails') :
            todo = registration()
            todo.prefix = request.POST.get('prefix')
            todo.firstname = request.POST.get('firstname')
            todo.middlename = request.POST.get('middlename')
            todo.lastname = request.POST.get('lastname')
            todo.adhaarcardnumber = request.POST.get('adhaarcardnumber')
            todo.gender = request.POST.get('gender')
            todo.bloodgroup = request.POST.get('bloodgroup')
            todo.birthdate = request.POST.get('birthdate')
            todo.maritalstatus = request.POST.get('maritalstatus')
            todo.occupation = request.POST.get('occupation')
            todo.registrationdate = request.POST.get('registrationdate')
            todo.registrationtime = request.POST.get('registrationtime')
            todo.age = request.POST.get('age')
            todo.weight = request.POST.get('weight')
            todo.height = request.POST.get('height')
            todo.phonenumber = request.POST.get('phonenumber')
            todo.address1 = request.POST.get('address1')
            todo.address2 = request.POST.get('address2')
            todo.city = request.POST.get('city')
            todo.pincode = request.POST.get('pincode')
            todo.allergydetails = request.POST.get('allergydetails')

            todo.save()
            messages.success(request, ' data is saved successfully ..!')
            return render(request, 'registration.html')

    else:
        return render(request, 'registration.html')

# def Editopdcomplain(request:HttpRequest,id):
#     editempobj=opdcomplainmodel.objects.get(id=id)
#     return render(request,'opdcomplain.html',{"opdcomplainmodel":editempobj})

# def updateopdcomplain(request:HttpRequest,id):
#     Updateemp=opdcomplainmodel.objects.get(id=id)
#     fo=Empforms(request.POST,instance=Updateemp)
#     if fo.is_valid():
#         fo.save()
#         messages.success(request,'record updated successfully ..!')
#         return render(request,'opdcomplain.html',{"opdcomplainmodel":Updateemp})


# def Delopdcomplain(request,id):
#     delopdcomplain=opdcomplainmodel.objects.get(id=id)
#     delopdcomplain.delete()
#     showdata=opdcomplainmodel.objects.all()
#     return render(request,'opdcomplain.html',{"data":showdata})
