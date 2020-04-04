from django.contrib import admin
from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.Aval.as_view(), name='header_render'),
    path('<str:link_id>/', views.Check.get_check, name='get_check'),
]