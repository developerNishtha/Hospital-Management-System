"""opd_pfsh URL Configuration

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
    path('', views.showopd_pfsh,name='showopd_pfsh'),
    path('Insertopd_pfsh', views.Insertopd_pfsh,name='Insertopd_pfsh'),
    path('Edit/<int:id>', views.Editopd_pfsh,name='Editopd_pfsh'),
   # path('Update/<int:id>', views.updateempopd_pfsh,name='updateempopd_pfsh'),
    path('Delete/<int:id>', views.Delempopd_pfsh,name='Delempopd_pfsh'),
]