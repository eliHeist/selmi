from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from projects.admin import useradmin

urlpatterns = [
    path('superadmin/', admin.site.urls),
    path('admin/', useradmin.urls),
    path('projects/', include('projects.urls', namespace='projects')),
    path('bookings/', include('bookings.urls', namespace='bookings')),
    path('', include('main.urls', namespace='main')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)