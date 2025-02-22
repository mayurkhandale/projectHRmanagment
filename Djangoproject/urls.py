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
from django.urls import path,include
from  hradmin import urls as adminurl
from manager import urls as managerurl
from  applicant import urls as applicanturl
from django.views.generic import TemplateView
urlpatterns = [
    path('hradmin/', admin.site.urls),
    path('',include(adminurl)),
    path('',include(managerurl)),
    path('',include(applicanturl)),

    path('home/',TemplateView.as_view(template_name="home.html"),name="home")
]
