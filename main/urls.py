from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='homepage'),
    path('services/', views.ServiceView.as_view(), name='services'),
    path('about/', views.AboutView.as_view(), name='about'),
]