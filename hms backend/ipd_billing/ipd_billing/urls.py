"""ipd_billing URL Configuration

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
    path('', views.showipd_billing,name='showipd_billing'),
    path('Insertipd_billing', views.Insertipd_billing,name='Insertipd_billing'),
    path('Edit/<int:id>', views.Editipd_billing,name='Editipd_billing'),
    path('Update/<int:id>', views.updateipd_billing,name='updateipd_billing'),
    path('Delete/<int:id>', views.Delipd_billing,name='Delipd_billing'),
]

