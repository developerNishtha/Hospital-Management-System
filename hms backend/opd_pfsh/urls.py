from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.showopd_pfsh,name='showopd_pfsh'),
    path('Insertopd_pfsh/<int:UHIDid>', views.Insertopd_pfsh,name='Insertopd_pfsh'),
    path('Edit/<int:id>', views.Editopd_pfsh,name='Editopd_pfsh'),
    path('Update/<int:id>', views.updateempopd_pfsh,name='updateempopd_pfsh'),
    path('Delete/<int:id>', views.Delempopd_pfsh,name='Delempopd_pfsh'),
]