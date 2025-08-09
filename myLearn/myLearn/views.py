# from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("This is the Home Page!")
    return render(request, 'myLearn/home.html')

def about(request):
    # return HttpResponse("This is the About Page!")
    return render(request, 'myLearn/about.html')
