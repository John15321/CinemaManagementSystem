from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('cpl/', views.cpl),
    path('kdm/', views.kdm),
    path('spl/', views.spl),

]

