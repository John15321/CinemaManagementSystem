from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUSerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ShowForm(ModelForm):
    class Meta:
        model = Show
        fields = ['name','SPLs','start_date']

class CinemaHallForm(ModelForm):
    class Meta:
        model = CinemaHall
        fields = '__all__'

class SoundSystemForm(ModelForm):
    class Meta:
        model = SoundSystem
        fields = '__all__'

class ProjectorForm(ModelForm):
    class Meta:
        model = Projector
        fields = '__all__'

class SPLForm(ModelForm):
    class Meta:
        model = SPL
        fields = '__all__'

class CPLForm(ModelForm):
    class Meta:
        model = CPL
        fields = '__all__'

class EffectForm(ModelForm):
    class Meta:
        model = Effect
        fields = '__all__'

class KDMForm(ModelForm):
    class Meta:
        model = KDM
        fields = '__all__'