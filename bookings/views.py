from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from rest_framework.response import Response

from bookings.forms import BookingForm

# Create your views here.
class BookingView(View):
    template_name = 'bookings/bookings.html'
    def get(self, request, *args, **kwargs):
        context = {
            'form': BookingForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        print('\nPOST\n')
        form = BookingForm(request.POST)
        if form.is_valid():
            print('valid form')
            form.save()
            print('valid form saved')
        else:
            print('invalid form')
            context = {
                'form': form,
            }
            return render(request, self.template_name, context)
        return HttpResponseRedirect(reverse('bookings:success-page'))

class SuccessView(View):
    def get(self, request):
        template_name = 'bookings/success.html'
        context = {}
        return render(request, template_name, context)


def sendMessage(data):
    html_message = render_to_string('contact/components/mail_template.html', {'name': data.get('name'), 'email': data.get('email'), 'message': data.get('message')})

    try:
        send_mail(
        subject=f"Message from {data.get('name')}",
        message='',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=settings.TO_EMAILS,
        html_message=html_message
        )

        return Response('SUCCESS')
    except Exception as e:
        print(f'Exception: {e}')
        return Response('Failed, try again later')
