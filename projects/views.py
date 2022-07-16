from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def projects(request):
    return HttpResponse("Hi.. Im muthu")