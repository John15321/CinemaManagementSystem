from django.db import models
from django.utils.timezone import now

class KDM(models.Model):
    name = models.CharField(max_length=200)
    not_valid_before = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True,default=now)
    not_valid_after = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True,default=now)
    KDMKey = models.IntegerField(null=False)

    def __str__(self):
        return self.name


class CPL(models.Model):
    name = models.CharField(max_length=200)
    subtitles = models.CharField(max_length=200)
    duration = models.IntegerField(null=False)
    disk_size = models.IntegerField(null=False)
    KDM = models.ForeignKey(KDM, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Effect(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    duration = models.IntegerField(null=False)

    def __str__(self):
        return self.name

class SPL(models.Model):
    name = models.CharField(max_length=200)
    Effects = models.ManyToManyField(Effect, blank = True)
    CPLs  = models.ManyToManyField(CPL, blank=True)

    def __str__(self):
        return self.name


class Projector(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    resolution = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SoundSystem(models.Model):
    name = models.CharField(max_length=200)
    technology = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Show(models.Model):
    name = models.CharField(max_length=200)
    SPLs = models.ManyToManyField(SPL)
    cinema_hall = models.ForeignKey("CinemaHall", blank=True, null=True, on_delete=models.SET_NULL)
    start_date = models.DateTimeField(auto_now_add=False, auto_now=False, default=now)
    def __str__(self):
        return self.name

class CinemaHall(models.Model):
    name = models.CharField(max_length=200)
    showings = models.ManyToManyField(Show,blank=True)
    projector = models.ForeignKey(Projector, blank=True, null=True,on_delete=models.SET_NULL)
    sound_system = models.ForeignKey(SoundSystem, blank=True, null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name