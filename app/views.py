from django.shortcuts import render
from .models import UbeaeatsDailyEntry, UbeaeatsWeeklyEntry

# Create your views here.
def index(request):
    return render(request,"index.html")

def ubeaeats_daily_entry_view(request):
    # Query the database to get all entries
    daily_entries = UbeaeatsDailyEntry.objects.all()

    # You can pass 'entries' to the template for rendering
    return render(request, 'ubeaeats_daily_entry.html', {'daily_entries': daily_entries})

def ubeaeats_weekly_entry_view(request):
    # Query the database to get all entries
    weekly_entries = UbeaeatsWeeklyEntry.objects.all()

    # You can pass 'weekly_entries' to the template for rendering
    return render(request, 'ubeaeats_weekly_entry.html', {'weekly_entries': weekly_entries})
