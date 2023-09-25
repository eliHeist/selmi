from django.urls.base import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from .models import Project

# Create your views here.
class ProjectListView(ListView):
    template_name = 'projects/project_list.html'
    queryset = Project.objects.all().order_by('-date')
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    template_name = 'projects/project_detail.html'
    queryset = Project.objects.all()
    context_object_name = 'project'

