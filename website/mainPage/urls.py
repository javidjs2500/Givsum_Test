from django.contrib import admin
from django.urls import path
from . import views


app_name = "mainPage"
urlpatterns = [
    path('', views.index, name = 'index'),
    path('events/', views.events, name = 'events'),
]
