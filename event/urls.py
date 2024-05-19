from django.urls import path
from .views import index, speaker_details, form_email_send

urlpatterns = [
    path('', index, name='home'),
    path('speaker-details/<int:id>', speaker_details, name='speaker-details'),
    path('email-send/', form_email_send, name='email-send'),
]