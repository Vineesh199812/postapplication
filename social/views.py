from django.shortcuts import render
from django.views.generic import View
# Create your views here.

# localhost:8000/social.com/login
# get
class LoginView(View):

    def get(self,request,*args,**kwargs):
        return render(request,"login.html")
    def post(self,request,*args,**kwargs):
        print(request.POST)
        return render(request, "login.html")


class RegisterView(View):

    def get(self,request,*args,**kwargs):
        return render(request,"registration.html")
    def post(self,request,*args,**kwargs):
        print(request.POST)
        return render(request, "registration.html")
