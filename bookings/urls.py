from django.urls import path

from bookings import views

app_name = 'bookings'

urlpatterns = [
    path('', views.BookingView.as_view(), name='booking-page'),
    path('success/', views.SuccessView.as_view(), name='success-page'),
]