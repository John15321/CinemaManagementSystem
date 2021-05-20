from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shows/', views.shows, name='shows'),
    path('show/<str:pk>/', views.show, name='show'),
    path('projectors/', views.projectors, name='projectors'),
    path('cinemahall/<str:pk>', views.cinemahall, name='cinemahall'),
    path('cinemahalls/', views.cinemahalls, name='cinemahalls'),
    path('soundsystems/', views.soundsystems, name='soundsystems'),
    path('creatshow/', views.creatShow, name='creatshow'),
    path('updateshow/<str:pk>/', views.updateShow, name='updateshow'),
    path('deleteshow/<str:pk>/', views.deleteShow, name='deleteshow'),
    path('addprojector/', views.addprojector, name='addprojector'),
    path('deleteprojector/<str:pk>/', views.deleteprojector, name='deleteprojector'),
    path('addsoundsystem/', views.addsoundsystem, name='addsoundsystem'),
    path('deletesoundsystem/<str:pk>/', views.deletesoundsystem, name='deletesoundsystem'),
    path('addcinemahall/', views.addcinemahall, name='addcinemahall'),
    path('deletecinemahall/<str:pk>/', views.deletecinemahall, name='deletecinemahall'),
    path('updatecinemahall/<str:pk>/', views.updatecinemahall, name='updatecinemahll'),
]

