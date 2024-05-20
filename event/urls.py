from django.urls import path
from .views import index, speaker_details, form_email_send, order_tickets

urlpatterns = [
    path('', index, name='home'),
    path('email-send/', form_email_send, name='email-send'),
    path('order-tickets/', order_tickets, name='order-tickets'),
    path('speaker-details/<int:id>', speaker_details, name='speaker-details'),
]