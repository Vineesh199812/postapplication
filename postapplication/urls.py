"""postapplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from postapi import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
router=DefaultRouter()
router.register("api/v1/accounts/register",views.UserRegistrationView,basename="registration")
router.register("api/v1/users/profile",views.UserProfileView,basename="profile")
router.register("api/v1/post",views.PostView,basename="post")
#router.register("api/v1/post/<int:id/add_comment",views.PostView,basename="comment")
#api/v1/users/profile
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/token/",TokenObtainPairView.as_view()),
    path("api/v1/token/refresh/",TokenRefreshView.as_view()),
]+router.urls