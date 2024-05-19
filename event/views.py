from django.shortcuts import render, redirect
from .models import Speakers, Hotels, Gallery, Sponsors, Tickets, Schedule
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

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
def speaker_details(request, id):
    speaker = Speakers.objects.get(id=id)
    return render(request, 'speaker-details.html', {'speaker': speaker})

@login_required(login_url="login")
def form_email_send(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = f"Thank you for contacting with us {name} ."
        # code to send email
        send_mail(
            'Contact us', message, 'settings.EMAIL_HOST_USER', [email], fail_silently=False)
        return redirect('home')
    return render(request, 'index.html')