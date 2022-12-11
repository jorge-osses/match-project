from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.db import IntegrityError
from django.views.generic.base import TemplateView
from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms


class HomePageView(TemplateView):
    template_name = 'base/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Match"
        return context



# class DashboardView(TemplateView):
#     template_name = "base/dashboard.html"

#     def get(self, request, *args, **kwargs):
#         displaynames = User.objects.all()
#         return render(request, self.template_name, {'displayusername': displaynames})

