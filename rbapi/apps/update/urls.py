from django.contrib import admin
from django.urls import path
from . import views

app_name = 'update'

urlpatterns = [
    path('', views.UpdateBase.as_view(), name='update_base'),
]