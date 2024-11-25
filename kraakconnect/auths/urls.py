from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.mylogin, name="login"),
    path('success', views.succes, name="success"),
]
