from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('ubeaeats_daily_entry/', views.ubeaeats_daily_entry_view, name='ubeaeats_daily_entry'),
    path('ubeaeats_weekly_entry/', views.ubeaeats_weekly_entry_view, name='ubeaeats_weekly_entry'),

]