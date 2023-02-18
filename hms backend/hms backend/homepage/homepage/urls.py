"""homepage URL Configuration

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
from django.urls import path,include
from . import views
from opdcomplain import views as vi_opdcomplain

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showhomepage,name='showhomepage'),
    path('Inserthomepage', views.Inserthomepage,name='Inserthomepage'),
    path('Edit/<int:id>', views.Edithomepage,name='Edithomepage'),    
    path('Up/<int:id>', views.updatehomepage,name='updatehomepage'),
    path('Delete/<int:id>', views.Delhomepage,name='Delhomepage'),

    path('opdcomplain/',include('opdcomplain.urls')),
    path('updateopdcomplain/<int:id>', vi_opdcomplain.updateopdcomplain,name='updateopdcomplain'),

    path('round_notes/',include('round_notes.urls')),
]
