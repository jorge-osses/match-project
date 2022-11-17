from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic.base import TemplateView


# Create your views here.
class RegisterView(TemplateView):
    template_name = "register/register.html"
