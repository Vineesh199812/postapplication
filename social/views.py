from django.shortcuts import render
from django.views.generic import View
# Create your views here.

# localhost:8000/social.com/login
# get
class LoginView(View):

    def get(self,request,*args,**kwargs):
        return render(request,"login.html")
    # def post(self,request,*args,**kwargs):
    #     pass

class RegisterView(View):

    def get(self,request,*args,**kwargs):
        return render(request,"registration.html")