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
from app1 import views
from hradmin import views
urlpatterns = [
    path('login/', views.LoginPage.as_view(), name="login"),
    path('add/', views.AddEmp.as_view(), name="add"),
    path('viewemp/',views.Viewemp,name="viewemp"),
    path('updateemp/',views.Updateemp,name="updateemp"),
    path('update/<int:pk>',views.Update_Emp_Details.as_view(),name="update"),
    path('deleteemp/',views.Deleteemp.as_view(),name="deleteemp")
]
