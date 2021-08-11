from WorldCountries import views
from WorldCountries.models import WorldCountries
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from WorldCountries import views
urlpatterns = [

    
    path('',views.index,name='index'),
  
]
