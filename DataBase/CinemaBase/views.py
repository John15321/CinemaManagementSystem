from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.timezone import timedelta, utc
from django.utils import dateformat
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import datetime


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import *
from .decorators import *


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    content={}
    return render(request, 'CinemaBase/login.html',content)

def logoutUser(request):
    logout((request))
    return redirect('login')

def registerPage(request):
    form = CreateUSerForm()
    content={"form":form}

    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created!')
            return redirect('login')

    return render(request, 'CinemaBase/register.html',content)


@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
def home(request):
    cinema_list = CinemaHall.objects.all()
    current_show_list = {}
    time_left_list = {}
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    for hall in cinema_list:
        for show in hall.showings.all():
            duration = 0
            for spl in show.SPLs.all():
                for cpl in spl.CPLs.all():
                    duration = duration + cpl.duration
                for effect in spl.Effects.all():
                    duration = duration + effect.duration
            if now >= show.start_date and now <= show.start_date + timedelta(seconds=duration):
                current_show_list[hall.id] = show.name
                time_left_list[hall.id] = str(show.start_date + timedelta(seconds=duration) - now).split('.')[0]

    content = {'cinema_list': cinema_list, 'current_show_list': current_show_list, 'time_left_list': time_left_list}
    return render(request, 'CinemaBase/dashboard.html', content)

@login_required(login_url='login')
def permission(request):
    return render(request, 'CinemaBase/permission.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
def show(request, pk):
    show = Show.objects.get(id=pk)
    spls = show.SPLs.all()
    content = {'show':show, 'spls':spls}
    return render(request, 'CinemaBase/show.html', content)

@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
def creatShow(request):
    form = ShowForm()
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/shows')

    content = {'form':form}
    return render(request, 'CinemaBase/formpage.html', content)

@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
def updateShow(request,pk):
    show = Show.objects.get(id=pk)
    form = ShowForm(instance=show)
    if request.method == 'POST':
        form = ShowForm(request.POST, instance=show)
        if form.is_valid():
            form.save()
            return redirect('/shows')
    content = {'form': form}
    return render(request, 'CinemaBase/formpage.html', content)

@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
def deleteShow(request,pk):
    show = Show.objects.get(id=pk)
    back_address = 'shows'
    delete_action = 'deleteshow'
    if request.method == 'POST':
        show.delete()
        return redirect('/shows')
    content = {'item':show, 'back_address': back_address , 'delete_action':delete_action}
    return render(request, 'CinemaBase/delete.html', content)

@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
def cinemahalls(request):
    cinema_list = CinemaHall.objects.all()
    content = {'cinema_list': cinema_list}
    return render(request, 'CinemaBase/cinemahalls.html',content)

@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
def cinemahall(request,pk):
    cinema_hall = CinemaHall.objects.get(id=pk)
    show_list = cinema_hall.showings.all()
    content = {'cinema_hall': cinema_hall, 'show_list':show_list}
    return render(request, 'CinemaBase/cinemahall.html',content)

@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
def addcinemahall(request):
    form = CinemaHallForm()
    if request.method == 'POST':
        form = CinemaHallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cinemahalls')

    content = {'form': form}
    return render(request, 'CinemaBase/formpage.html', content)

@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
def updatecinemahall(request,pk):
    cinemahall = CinemaHall.objects.get(id=pk)
    form = CinemaHallForm(instance=cinemahall)
    if request.method == 'POST':
        form = CinemaHallForm(request.POST, instance=cinemahall)
        if form.is_valid():
            form.save()
            return redirect('/cinemahalls')
    content = {'form': form}
    return render(request, 'CinemaBase/formpage.html', content)

@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
def deletecinemahall(request,pk):
    cinemahall = CinemaHall.objects.get(id=pk)
    back_address = 'cinemahalls'
    delete_action = 'deletecinemahall'
    if request.method == 'POST':
        cinemahall.delete()
        return redirect('/cinemahalls')
    content = {'item': cinemahall, 'back_address': back_address , 'delete_action':delete_action}
    return render(request, 'CinemaBase/delete.html', content)

@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
def projectors(request):
    projector_list = Projector.objects.all()

    content = {'projector_list':projector_list}
    return render(request, 'CinemaBase/projectors.html',content)

@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
def addprojector(request):
    form = ProjectorForm()
    if request.method == 'POST':
        form = ProjectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/projectors')

    content = {'form': form}
    return render(request, 'CinemaBase/formpage.html', content)

@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
def deleteprojector(request,pk):
    projector = Projector.objects.get(id=pk)
    back_address = 'projectors'
    delete_action = 'deleteprojector'
    if request.method == 'POST':
        projector.delete()
        return redirect('/projectors')
    content = {'item': projector, 'back_address': back_address , 'delete_action':delete_action}
    return render(request, 'CinemaBase/delete.html', content)

@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
def soundsystems(request):
    soundsystem_list = SoundSystem.objects.all()

    content = {'soundsystem_list': soundsystem_list}
    return render(request, 'CinemaBase/soundsystems.html',content)

@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
def addsoundsystem(request):
    form = SoundSystemForm()
    if request.method == 'POST':
        form = SoundSystemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/soundsystems')

    content = {'form': form}
    return render(request, 'CinemaBase/formpage.html', content)

@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
def deletesoundsystem(request,pk):
    soundsystem = SoundSystem.objects.get(id=pk)
    back_address = 'soundsystems'
    delete_action = 'deletesoundsystem'
    if request.method == 'POST':
        soundsystem.delete()
        return redirect('/soundsystems')
    content = {'item': soundsystem, 'back_address': back_address , 'delete_action':delete_action}
    return render(request, 'CinemaBase/delete.html', content)

@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
def spls(request):
    spls_list = SPL.objects.all()
    duration_list ={}
    for spl in spls_list.all():
        duration=0
        for cpl in spl.CPLs.all():
            duration = duration + cpl.duration
        for effect in spl.Effects.all():
            duration = duration + effect.duration
        duration_list[spl.id] = timedelta(seconds=duration)
    content = {'spls_list': spls_list, 'duration_time': duration_list}
    return render(request, 'CinemaBase/spls.html',content)

@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
def spl(request, pk):
    spl = SPL.objects.get(id=pk)
    cpls = spl.CPLs.all()
    effects = spl.Effects.all()
    content = {'spl':spl, 'cpls':cpls, 'effects':effects}
    return render(request, 'CinemaBase/spl.html', content)

@login_required(login_url='login')
@admin_only
def createspl(request):
    form = SPLForm()
    if request.method == 'POST':
        form = SPLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/spls')

    content = {'form':form}
    return render(request, 'CinemaBase/formpage.html', content)

@login_required(login_url='login')
@admin_only
def updatespl(request,pk):
    spl = SPL.objects.get(id=pk)
    form = SPLForm(instance=spl)
    if request.method == 'POST':
        form = SPLForm(request.POST, instance=spl)
        if form.is_valid():
            form.save()
            return redirect('/spls')
    content = {'form': form}
    return render(request, 'CinemaBase/formpage.html', content)

@login_required(login_url='login')
@admin_only
def deletespl(request,pk):
    spl = SPL.objects.get(id=pk)
    back_address = 'spls'
    delete_action = 'deletespl'
    if request.method == 'POST':
        spl.delete()
        return redirect('/spls')
    content = {'item':spl, 'back_address': back_address , 'delete_action':delete_action}
    return render(request, 'CinemaBase/delete.html', content)

@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
def cpls(request):
    cpls_list = CPL.objects.all()

    content = {'cpls_list': cpls_list}
    return render(request, 'CinemaBase/cpls.html',content)

@login_required(login_url='login')
@admin_only
def createcpl(request):
    form = CPLForm()
    if request.method == 'POST':
        form = CPLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cpls')

    content = {'form':form}
    return render(request, 'CinemaBase/formpage.html', content)

@login_required(login_url='login')
@admin_only
def updatecpl(request,pk):
    cpl = CPL.objects.get(id=pk)
    form = CPLForm(instance=cpl)
    if request.method == 'POST':
        form = CPLForm(request.POST, instance=cpl)
        if form.is_valid():
            form.save()
            return redirect('/cpls')
    content = {'form': form}
    return render(request, 'CinemaBase/formpage.html', content)

@login_required(login_url='login')
@admin_only
def deletecpl(request,pk):
    cpl = CPL.objects.get(id=pk)
    back_address = 'cpls'
    delete_action = 'deletecpl'
    if request.method == 'POST':
        cpl.delete()
        return redirect('/cpls')
    content = {'item':cpl, 'back_address': back_address , 'delete_action':delete_action}
    return render(request, 'CinemaBase/delete.html', content)

@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
def kdms(request):
    kdms_list = KDM.objects.all()

    content = {'kdms_list': kdms_list}
    return render(request, 'CinemaBase/kdms.html',content)

@login_required(login_url='login')
@admin_only
def createkdm(request):
    form = KDMForm()
    if request.method == 'POST':
        form = KDMForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/kdms')

    content = {'form':form}
    return render(request, 'CinemaBase/formpage.html', content)

@login_required(login_url='login')
@admin_only
def deletekdm(request,pk):
    kdm = KDM.objects.get(id=pk)
    back_address = 'kdms'
    delete_action = 'deletekdm'
    if request.method == 'POST':
        kdm.delete()
        return redirect('/kdms')
    content = {'item':kdm, 'back_address': back_address , 'delete_action':delete_action}
    return render(request, 'CinemaBase/delete.html', content)

@login_required(login_url='login')
@allowed_users(allowed_roles=["admins", "operators"])
def effects(request):
    effects_list = Effect.objects.all()

    content = {'effects_list': effects_list}
    return render(request, 'CinemaBase/effects.html',content)

@login_required(login_url='login')
@admin_only
def createeffect(request):
    form = EffectForm()
    if request.method == 'POST':
        form = EffectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/effects')

    content = {'form':form}
    return render(request, 'CinemaBase/formpage.html', content)

@login_required(login_url='login')
@admin_only
def deleteeffect(request,pk):
    effect = Effect.objects.get(id=pk)
    back_address = 'effects'
    delete_action = 'deleteeffect'
    if request.method == 'POST':
        effect.delete()
        return redirect('/effects')
    content = {'item':effect, 'back_address': back_address , 'delete_action':delete_action}
    return render(request, 'CinemaBase/delete.html', content)


