from django.shortcuts import render
from django.http import HttpResponse

def mypath(request):
    print("ppppppp")
    return HttpResponse(request)
    