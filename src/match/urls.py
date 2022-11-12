from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('base.urls')),
    path('admin/', admin.site.urls, name='Admin'),
]
# path('', views.home, name='home'),
# path('login/', views.login, name='login'),
# path('about/', views.about, name='about'),
# path('faq/', views.faq, name='faq'),
#path('register/', viewsregister.register, name='register'),
