from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.db import IntegrityError
from django.views.generic.base import TemplateView
from requests import Response
from register.models import Contact
from register.views import contact
# from django.contrib.auth.decorators import login_required


class HomePageView(TemplateView):
    template_name = 'base/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Match"
        return context


class FaqView(TemplateView):
    template_name = "base/faq.html"


class AboutView(TemplateView):
    template_name = "base/about.html"


class DashboardView(TemplateView):
    template_name = "base/dashboard.html"

    def get(self, request, *args, **kwargs):
        displaynames = User.objects.all()
        return render(request, self.template_name, {'displayusername': displaynames})


# class SignUpView(CreateView):
#     pass

def signup(request):

    if request.method == 'GET':
        return render(request, 'base/signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                # login(request, user)
                return redirect('signin')
            except IntegrityError:
                return render(request, 'base/signup.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                })

        return render(request, 'base/signup.html', {
            'form': UserCreationForm,
            'error': 'Password no coincide'
        })


def signin(request):
    if request.method == 'GET':
        return render(request, 'base/signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'base/signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o password incorrecto'
            })
        else:
            login(request, user)

            if Contact.objects.filter(user=request.user).exists():
                return redirect('dashboard')
            else:
                return redirect('contact')


def signout(request):
    logout(request)
    return redirect('home')
