from django.urls import path
from social import views

urlpatterns=[
    path("login",views.LoginView.as_view(),name="signin"),
    path("register",views.RegisterView.as_view(),name="signup"),
    path("home",views.IndexView.as_view(),name="index"),
    path("logout",views.SignOutView.as_view(),name="signout")
]



# new project == todo ==> todoapp ==> new model in models of todo with fields taskname,user,status,date