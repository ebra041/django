from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('regget/', views.register_get, name='regget'),
    path('regpost/', views.register_post, name='regpost'),
]