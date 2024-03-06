from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ubereats_daily_entry_view, name='home'),
    path('ubereats_daily_entry/', views.ubereats_daily_entry_view, name='ubereats_daily_entry'),
    path('ubereats_daily_je/', views.ubereats_daily_je_view, name='ubereats_daily_je'),
    path('ubereats_weekly_entry/', views.ubereats_weekly_entry_view, name='ubereats_weekly_entry'),
]