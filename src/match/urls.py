from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('base.urls')),
    path('admin/', admin.site.urls, name='Admin'),
]
# path('', views.home, name='home'),
#path('register/', viewsregister.register, name='register'),
