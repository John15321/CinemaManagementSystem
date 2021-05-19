from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'CinemaBase/dashboard.html')

def shows(request):
    return HttpResponse("Show Page")
