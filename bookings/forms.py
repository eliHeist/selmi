from typing import Any
from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.template.loader import render_to_string

from bookings.models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ['is_attended_to',]
    
    def save(self, commit: bool = True) -> Any:
        booking:Booking = super().save(commit=False)
        if commit:
            booking.save()
        
        sendEmails(booking)
            
        return super().save(commit)

def sendEmails(booking: Booking):
    # TODO send confirmation email to user
    subject = 'Booking Confirmation'
    receipeint_list = [booking.email]
    template = render_to_string('bookings/templates/confirm-booking.html', {'booking': booking})
    send_mail(subject, '', settings.DEFAULT_FROM_EMAIL, receipeint_list, html_message=template)

    # TODO send email to alert admin
    subject = 'Booking Confirmation'
    receipeint_list = settings.TO_EMAILS
    template = render_to_string('bookings/templates/notify-booking.html', {'booking': booking})
    send_mail(subject, '', settings.DEFAULT_FROM_EMAIL, receipeint_list, html_message=template)

