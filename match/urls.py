from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('', include('base.urls')),
    path('admin/', admin.site.urls, name='Admin'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
