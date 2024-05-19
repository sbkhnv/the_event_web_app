from django.urls import path
from .views import index, speaker_details

urlpatterns = [
    path('', index, name='home'),
    path('speaker-details/', speaker_details, name='speaker-details'),
]