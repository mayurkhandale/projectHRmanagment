from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from .form import RegistrationForm
from .models import RegistrationModel
from .form import ApplicationForm
from .models import ApplicationformModel
# Create your views here.
class aplicant_login(View):
    def get(self,request):
        return render(request,"Applicant/applicantlogin.html")
    def post(self,request):
        if request.POST:
           auser=request.POST["aun"]
           apassword=request.POST["aup"]
           if auser=="applicant" and apassword=="applicant":
              save="successfully saved"
              return render(request,"applicant/applicantsucess.html",{"save":save,"set":set})
           else:
               messages.error(request,"Invalid Details")
               return redirect('aplicant_login')

class applicant_reg(View):
    def get(self,request):
        set=RegistrationForm()
        return render(request,"Applicant/register.html",{"set":set})
    def post(self,request):
        ap=RegistrationForm(request.POST)
        if ap.is_valid():
            ap.save()
            messages.success(request,"sucessfully Registation")
            return render(request,"Applicant/datalogin.html")
class datalogin(View):
    def get(self,request):
        #username=RegistrationModel.objects.filter()
        return render(request,"Applicant/datalogin.html")
    def post(self,request):
            us = request.POST.get('user')
            pw=request.POST.get('password')
            if RegistrationModel.objects.filter(username=us):
             if RegistrationModel.objects.filter(password=pw):
                res = RegistrationModel.objects.get(username=us)
                apform=ApplicationForm()
                messages.success(request,"successfully login")
                return render(request,"Applicant/applicationform.html",{"data":res,"apform":apform})
             else:
                  messages.error(request, "invalid username and password")
                  return redirect('datalogin')
            else:
                messages.error(request,"invalid username and password")
                return redirect('datalogin')


