"""round_notes URL Configuration

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
    path('', views.showround_notes,name='showround_notes'),
    path('Insertround_notes', views.Insertround_notes,name='Insertround_notes'),
#     path('Edit/<int:id>', views.Editround_notes,name='Editround_notes'),
#     path('Update/<int:id>', views.updateround_notes,name='updateround_notes'),
    path('Delete/<int:id>', views.Delround_notes,name='Delround_notes'),
]
