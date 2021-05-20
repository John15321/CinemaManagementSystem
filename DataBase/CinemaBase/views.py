from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.timezone import timedelta

# Create your views here.
from .models import *
from .forms import *

def home(request):
    return render(request, 'CinemaBase/dashboard.html')

def shows(request):
    shows_list = Show.objects.all()
    end_date_list ={}
    for show in shows_list:
        duration = 0
        for spl in show.SPLs.all():
            for cpl in spl.CPLs.all():
                duration = duration + cpl.duration
            for effect in spl.Effects.all():
                duration = duration + effect.duration
        end_date_list[show.id] = show.start_date + timedelta(seconds=duration)
    content = {'shows_list': shows_list, 'end_date_time': end_date_list}
    return render(request, 'CinemaBase/shows.html',content)

def show(request, pk):
    show = Show.objects.get(id=pk)
    spls = show.SPLs.all()
    content = {'show':show, 'spls':spls}
    return render(request, 'CinemaBase/show.html', content)

def creatShow(request):
    form = ShowForm()
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/shows')

    content = {'form':form}
    return render(request,'CinemaBase/showform.html',content)

def updateShow(request,pk):
    show = Show.objects.get(id=pk)
    form = ShowForm(instance=show)
    if request.method == 'POST':
        form = ShowForm(request.POST, instance=show)
        if form.is_valid():
            form.save()
            return redirect('/shows')
    content = {'form': form}
    return render(request, 'CinemaBase/showform.html', content)

def deleteShow(request,pk):
    show = Show.objects.get(id=pk)
    if request.method == 'POST':
        show.delete()
        return redirect('/shows')
    content = {'item':show}
    return render(request, 'CinemaBase/delete.html', content)

def cinemahalls(request):
    cinema_list = CinemaHall.objects.all()

    content = {'cinema_list': cinema_list}
    return render(request, 'CinemaBase/cinemahalls.html',content)

def cinemahall(request,pk):
    cinema_hall = CinemaHall.objects.get(id=pk)
    show_list = cinema_hall.showings.all()
    content = {'cinema_hall': cinema_hall, 'show_list':show_list}
    return render(request, 'CinemaBase/cinemahall.html',content)

def addcinemahall(request):
    form = CinemaHallForm()
    if request.method == 'POST':
        form = CinemaHallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cinemahalls')

    content = {'form': form}
    return render(request, 'CinemaBase/cinemahallform.html', content)

def updatecinemahall(request,pk):
    cinemahall = CinemaHall.objects.get(id=pk)
    form = CinemaHallForm(instance=cinemahall)
    if request.method == 'POST':
        form = CinemaHallForm(request.POST, instance=cinemahall)
        if form.is_valid():
            form.save()
            return redirect('/cinemahalls')
    content = {'form': form}
    return render(request, 'CinemaBase/cinemahallform.html', content)

def deletecinemahall(request,pk):
    cinemahall = CinemaHall.objects.get(id=pk)
    if request.method == 'POST':
        cinemahall.delete()
        return redirect('/cinemahalls')
    content = {'item': cinemahall}
    return render(request, 'CinemaBase/deletecinemahall.html', content)

def projectors(request):
    projector_list = Projector.objects.all()

    content = {'projector_list':projector_list}
    return render(request, 'CinemaBase/projectors.html',content)

def addprojector(request):
    form = ProjectorForm()
    if request.method == 'POST':
        form = ProjectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/projectors')

    content = {'form': form}
    return render(request, 'CinemaBase/projectorform.html', content)

def deleteprojector(request,pk):
    projector = Projector.objects.get(id=pk)
    if request.method == 'POST':
        projector.delete()
        return redirect('/projectors')
    content = {'item': projector}
    return render(request, 'CinemaBase/deleteprojector.html', content)

def soundsystems(request):
    soundsystem_list = SoundSystem.objects.all()

    content = {'soundsystem_list': soundsystem_list}
    return render(request, 'CinemaBase/soundsystems.html',content)

def addsoundsystem(request):
    form = SoundSystemForm()
    if request.method == 'POST':
        form = SoundSystemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/soundsystems')

    content = {'form': form}
    return render(request, 'CinemaBase/soundsystemsform.html', content)

def deletesoundsystem(request,pk):
    soundsystem = SoundSystem.objects.get(id=pk)
    if request.method == 'POST':
        soundsystem.delete()
        return redirect('/soundsystems')
    content = {'item': soundsystem}
    return render(request, 'CinemaBase/deletesoundsystem.html', content)

