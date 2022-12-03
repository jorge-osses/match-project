from django.contrib import admin
from django.urls import path
# from .views import RegisterView
from .views import contact

urlpatterns = [
    path('contact/', contact, name='contact'),
]

# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register')
# ]
