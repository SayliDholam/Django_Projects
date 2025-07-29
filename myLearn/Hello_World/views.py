from django.shortcuts import render
from django.http import HttpResponse

def say_HelloWorld(request):
    return HttpResponse("Hello, World!")