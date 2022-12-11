from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('base.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('dashboard/', include('dashboard.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
