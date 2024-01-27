from django.shortcuts import render
from django.contrib import admin
from django.urls import path,include
from .views import weather_view

urlpatterns = [
    path('',weather_view,name="city_weather"),
]