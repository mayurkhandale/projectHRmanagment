from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View
from hradmin.form import Employeeform
from hradmin.models import AddEmployee
from django.views.generic import UpdateView,DeleteView


# Create your views here.

class LoginPage(View):
        def get(self, request):
            return render(request, "admin/adminlogin.html")

        def post(self, request):
            u = request.POST.get("t1")
            p = request.POST.get("t2")
            if u == "mayur" and p == "mayur@123":
                messages.success(request,"information save")
                return render(request,"admin/loginsuccess.html")

            else:

              return render(request, "admin/adminlogin.html",{"error":"invalid username & password"})

class AddEmp(View):
    def get(self,request):
        form=Employeeform()
        return render(request, "admin/addemp.html",{"form":form})

    def post(self,request):
        ef=Employeeform(request.POST)
        if ef.is_valid():
            ef.save()
            messages.success(request,"succesfully saved")
            return redirect("add")
        else:
            return render(request,"admin/addemp.html")

def Viewemp(request):
    emp=AddEmployee.objects.all()
    return render(request,"Admin/viewemp.html",{"emp":emp})

def Updateemp(request):
    update=AddEmployee.objects.all()
    return render(request,"Admin/updateemp.html",{"update":update})

class  Update_Emp_Details(UpdateView):
       template_name = "Admin/update_emp_details.html"
       model = AddEmployee
       fields = '__all__'
       success_url = '/updateemp/'

class Deleteemp(View):
      def get(self,request):
        return render(request,'admin/deleteemp.html',{"data":AddEmployee.objects.all()})
      def post(self,request):
          idlist=request.POST.get("del")
          AddEmployee.objects.filter(empployee_id=idlist).delete()
          return render(request,'Admin/deleteemp.html',{"data":AddEmployee.objects.all()})
