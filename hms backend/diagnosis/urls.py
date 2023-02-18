from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.showempdiagnosis,name='showempdiagnosis'),
    path('Insertempdiagnosis/<int:UHIDid>', views.Insertempdiagnosis,name='Insertempdiagnosis'),
    path('Edit/<int:id>', views.Editempopddiagnosis,name='Editempopddiagnosis'),
    path('Update_diagnosis/<int:id>', views.updateempopddiagnosis,name='updateempopddiagnosis'),
    
    path('Delete/<int:id>', views.Delempopddiagnosis,name='Delempopddiagnosis'),
    
]