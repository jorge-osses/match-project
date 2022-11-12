from django.urls import path
from .views import HomePageView, FaqView, AboutView, LoginView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('login/', LoginView.as_view(), name='login'),


]
