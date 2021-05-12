from django.db import models


class KDM(models.Model):
    name = models.CharField(max_length=200)
    not_valid_before = models.DateTimeField(auto_now_add=False, auto_now=False,blank=True)
    not_valid_after = models.DateTimeField(auto_now_add=False, auto_now=False,blank=True)
    KDMKey = models.IntegerField(null=False)


class CPL(models.Model):
    name = models.CharField(max_length=200)
    subtitles = models.CharField(max_length=200)
    duration = models.IntegerField(null=False)
    disk_size = models.IntegerField(null=False)
    KDM = models.ForeignKey(KDM,null=True,on_delete=models.SET_NULL)

class Effect(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    duration = models.IntegerField(null=False)

class SPL(models.Model):
    name = models.CharField(max_length=200)
    Effects = models.ManyToManyField(Effect)
    CPLs  = models.ManyToManyField(CPL)

class Show(models.Model):
    name = models.CharField(max_length=200)
    SPLs = models.ManyToManyField(SPL)
    cinema_hall = models.ForeignKey(KDM, null=True, on_delete=models.SET_NULL)

class Projector(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    resolution = models.CharField(max_length=200)

class SoundSystem(models.Model):
    name = models.CharField(max_length=200)
    technology = models.CharField(max_length=200)


class CinemaHall(models.Model):
    name = models.CharField(max_length=200)
    showings  = models.ManyToManyField(Show)
    projector = models.ForeignKey(Projector, null=True, on_delete=models.SET_NULL)
    sound_system = models.ForeignKey(SoundSystem, null=True, on_delete=models.SET_NULL)