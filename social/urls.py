from django.urls import path
from social import views

urlpatterns=[
    path("login",views.LoginView.as_view()),
    path("register",views.RegisterView.as_view())
]



# new project == todo ==> todoapp ==> new model in models of todo with fields taskname,user,status,date