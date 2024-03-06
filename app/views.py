from django.shortcuts import render
from .models import ubereatsDailyEntry, ubereatsWeeklyEntry, UbereatsDailyJE

# Create your views here.
def index(request):
    return render(request,"index.html")

def ubereats_daily_entry_view(request):
    # Query the database to get all entries
    daily_entries = ubereatsDailyEntry.objects.all()
    # You can pass 'entries' to the template for rendering
    return render(request, 'ubereats_daily_entry.html', {'daily_entries': daily_entries})


def ubereats_daily_je_view(request):
    # Query the database to get all entries
    daily_je = UbereatsDailyJE.objects.all()[:100]
    # You can pass 'entries' to the template for rendering
    return render(request, 'ubereats_daily_je.html', {'daily_je': daily_je})


def ubereats_weekly_entry_view(request):
    # Query the database to get all entries
    weekly_entries = ubereatsWeeklyEntry.objects.all()

    # You can pass 'weekly_entries' to the template for rendering
    return render(request, 'ubereats_weekly_entry.html', {'weekly_entries': weekly_entries})
