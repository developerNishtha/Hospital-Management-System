"""crudoperation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showopd_examination,name='showopd_examination'),
    path('Insertopd_examination', views.Insertopd_examination,name='Insertopd_examination'),
    path('Edit/<int:id>', views.Editopd_examination,name='Editopd_examination'),
    path('Update/<int:id>', views.updateempopddiagnosis,name='updateempopddiagnosis'),
    # path('Delete/<int:id>', views.Delempopddiagnosis,name='Delempopddiagnosis'),
]
