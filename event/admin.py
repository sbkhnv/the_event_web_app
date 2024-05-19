from django.contrib import admin
from .models import *

admin.site.register([Speakers, Schedule, Hotels, Gallery, Sponsors, Tickets, TDescription, Schedule_day])

