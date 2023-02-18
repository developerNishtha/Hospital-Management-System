from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.showopdcomplain,name='showopdcomplain'),
    path('Insertopdcomplain/<int:UHIDid>', views.Insertopdcomplain,name='Insertopdcomplain'),
    path('Edit/<int:id>', views.Editopdcomplain,name='Editopdcomplain'),
    path('Update/<int:id>', views.updateopdcomplain,name='updateopdcomplain'),
    path('Delete/<int:id>', views.Delopdcomplain,name='Delopdcomplain'),
]
