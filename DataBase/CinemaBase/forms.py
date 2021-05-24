from django.forms import ModelForm
from .models import *

class ShowForm(ModelForm):
    class Meta:
        model = Show
        fields = '__all__'

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