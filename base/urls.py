from django.contrib import admin
from django.urls import path
from .views import HomePageView, FaqView, AboutView, signup, signin, signout, DashboardView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('signup/', signup, name="signup"),
    path('logout/', signout, name="logout"),
    path('signin/', signin, name="signin"),
]
