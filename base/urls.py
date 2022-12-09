from django.contrib import admin
from django.urls import path, re_path
from .views import HomePageView, SignUpView, signin, signout, DashboardView, Profile

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('logout/', signout, name="logout"),
    path('signin/', signin, name="signin"),
    path('<int:pk>/', Profile.as_view(), name='perfil')
]
