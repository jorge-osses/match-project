from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.db import IntegrityError
from django.views.generic.base import TemplateView
from register.models import Contact
# from django.contrib.auth.decorators import login_required
from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from register.models import Contact


class HomePageView(TemplateView):
    template_name = 'base/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Match"
        return context


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = "base/dashboard.html"

    def get(self, request, *args, **kwargs):
        displaynames = User.objects.all()
        return render(request, self.template_name, {'displayusername': displaynames})


class Profile(DetailView):
    model = Contact


class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'base/signup.html'

    def get_success_url(self):
        return reverse_lazy('signin') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        form.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'dirección de Email'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'repita la contraseña'})
        return form


# def signup(request):

#     if request.method == 'GET':
#         return render(request, 'base/signup.html', {
#             'form': UserCreationForm
#         })
#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.create_user(
#                     username=request.POST['username'], password=request.POST['password1'])
#                 user.save()
#                 # login(request, user)
#                 return redirect('signin')
#             except IntegrityError:
#                 return render(request, 'base/signup.html', {
#                     'form': UserCreationForm,
#                     'error': 'Usuario ya existe'
#                 })

#         return render(request, 'base/signup.html', {
#             'form': UserCreationForm,
#             'error': 'Password no coincide'
#         })


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
