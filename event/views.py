from django.shortcuts import render
from .models import Speakers, Hotels, Gallery, Sponsors, Tickets, Schedule
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def index(request):
    speakers = Speakers.objects.all()
    hotels = Hotels.objects.all()
    gallery = Gallery.objects.all()
    sponsors = Sponsors.objects.all()
    tickets = Tickets.objects.all()
    schedule = Schedule.objects.all()

    return render(request, 'index.html', {'speakers': speakers, 'hotels': hotels, 'gallery': gallery, 'sponsors': sponsors, 'tickets': tickets, 'schedule': schedule})
@login_required(login_url="login")
def speaker_details(request):
    return render(request, 'speaker-details.html')
