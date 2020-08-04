from django.shortcuts import render,redirect
from django.views.generic import View
from  django.contrib import messages
from .models import New_reqModel
from .form import New_reqForm
from django.views.generic import UpdateView,DeleteView


# Create your views here.
class Managerlogin(View):
    def get(self,request):
        return render(request,"Manager/managerlogin.html")
    def post(self,request):
        muser=request.POST.get("m1")
        mpassword=request.POST.get("m2")
        if muser=="manager" and mpassword=="manager@123":
            messages.success(request,"succesfully Login")
            return render(request,"Manager/mlogins.html")
        else:
            messages.error(request,"invalid username & password")
            return redirect('home')
class New_req(View):
    def get(self,request):
        data=New_reqForm()
        return render(request,"manager/post_newreq.html",{"data":data})
    def post(self,request):
        pn=New_reqForm(request.POST)
        if pn.is_valid():
            pn.save()
            messages.success(request,"succesfully Added")
            return redirect('new_req')
        else:
            messages.error(request,"Fill the Form Correct follow the Instruction")
            return render(request,"manager/post_newreq.html")

class Modify(View):
    def get(self,request):
        return render(request,"manager/modify.html")
    def post(self,request):
        if request.method=="POST":
            try:
              opp=request.POST.get('t1')
              qs=New_reqModel.objects.get(opprtunity_code=opp)
              messages.success(request,"update sucessfully")
              return render(request,"manager/updatereq.html",{"qs":qs})
            except :
                messages.error(request,"data is not available")
                return render(request,"Manager/modify.html")

class update_req(UpdateView):
    template_name ="Manager/updatereq.html"
    model = New_reqModel
    fields = '__all__'
    success_url = '/update_req/'


class delete_req(DeleteView):
    def get(self,request):
        return render(request,"Manager/delete_req.html",{"record":New_reqModel.objects.all()})
    def post(self,request):
        delete=request.POST.get("delete")
        New_reqModel.objects.filter(opprtunity_code=delete).delete()
        return render(request,"Manager/delete_req.html",{"delete":New_reqModel.objects.all()})

class interview_shedule(View):
    def get(self,request):
        return render(request,"Manager/ishedule.html")







