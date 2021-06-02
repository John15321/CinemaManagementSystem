from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('register/',views.registerPage, name='register'),
    path('permission/', views.permission, name='permission'),
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
    path('spls/', views.spls, name='spls'),
    path('spl/<str:pk>/', views.spl, name='spl'),
    path('createspl/', views.createspl, name='createspl'),
    path('deletespl/<str:pk>/', views.deletespl, name='deletespl'),
    path('updatespl/<str:pk>/', views.updatespl, name='updatespl'),
    path('cpls/', views.cpls, name='cpls'),
    path('createcpl/', views.createcpl, name='createcpl'),
    path('deletecpl/<str:pk>/', views.deletecpl, name='deletecpl'),
    path('updatecpl/<str:pk>/', views.updatecpl, name='updatecpl'),
    path('kdms/', views.kdms, name='kdms'),
    path('createkdm/', views.createkdm, name='createkdm'),
    path('deletekdm/<str:pk>/', views.deletekdm, name='deletekdm'),
    path('effects/', views.effects, name='effects'),
    path('createeffect/', views.createeffect, name='createeffect'),
    path('deleteeffect/<str:pk>/', views.deleteeffect, name='deleteeffect'),


]

