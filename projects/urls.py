from projects.views import ProjectDetailView, ProjectListView
from django.urls import path


app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='detail'),
]
