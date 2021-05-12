from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'cinemabase/dashboard.html')

def spl(request):
    return render(request, 'cinemabase/spl.html')

def cpl(request):
    return render(request, 'cinemabase/cpl.html')

def kdm(request):
    return render(request, 'cinemabase/kdm.html')

def shows(request):
    return HttpResponse("Show Page")

def cinema_hall(request):
    return HttpResponse("Cinema Hall Page")

