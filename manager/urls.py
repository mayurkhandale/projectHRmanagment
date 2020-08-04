"""Djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from manager import views
from django.views.generic import TemplateView

urlpatterns = [
    path('managerlogin/', views.Managerlogin.as_view(),name="managerlogin"),
    path('managerhome/',TemplateView.as_view(template_name="Manager/reschedule.html"),name="managerhome"),
    path('new_req/',views.New_req.as_view(),name="new_req"),
    path('modify/',views.Modify.as_view(),name="modify"),
    path('updatereq<int:pk>/',views.update_req.as_view(),name="update_req"),
    path('delete_req/',views.delete_req.as_view(),name="delete_req"),
    path('shedule/',views.interview_shedule.as_view(),name="shedule")




]
