from projects.models import FeaturedProject, Photo, Project
from django.contrib import admin

# Register your models here.
admin.site.register(Project)
admin.site.register(FeaturedProject)
admin.site.register(Photo)

class UserAdmin(admin.AdminSite):
    site_header = 'Selmi Management Admin Area'
    site_title = 'Selmi Management'

useradmin = UserAdmin(name='Selmi User Admin')

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'date', 'services_offered', 'duration', 'location')
    list_filter = ('client', 'date', 'services_offered', 'location')
    search_fields = ('title', 'client', 'services_offered', 'location')
    inlines = [PhotoInline]

useradmin.register(Project, ProjectAdmin)