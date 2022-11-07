from django.contrib import admin
from django.urls import path
#from django.http import HttpResponse
#from register import views as viewsregister
from home import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('admin/', admin.site.urls, name='Admin'),
    #path('register/', viewsregister.register, name='register'),
]
