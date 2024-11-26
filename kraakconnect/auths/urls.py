from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.mylogin, name="loginName"),
    path('success', views.succes, name="successName"),
    path('register', views.Myregister, name="registerName")
]
