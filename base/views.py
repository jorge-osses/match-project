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


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = "base/dashboard.html"

    def get(self, request, *args, **kwargs):
        displaynames = User.objects.all()
        return render(request, self.template_name, {'displayusername': displaynames})


# class SignUpView(CreateView):
#     form_class = UserCreationFormWithEmail
#     template_name = 'base/signup.html'

#     def get_success_url(self):
#         return reverse_lazy('signin') + '?register'

#     def get_form(self, form_class=None):
#         form = super(SignUpView, self).get_form()
#         form.fields['username'].widget = forms.TextInput(
#             attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre de Usuario'})
#         form.fields['email'].widget = forms.EmailInput(
#             attrs={'class': 'form-control mb-2', 'placeholder': 'Dirección de Email'})
#         form.fields['password1'].widget = forms.PasswordInput(
#             attrs={'class': 'form-control mb-2', 'placeholder': 'Contraseña'})
#         form.fields['password2'].widget = forms.PasswordInput(
#             attrs={'class': 'form-control mb-2', 'placeholder': 'Repita la Contraseña'})
#         return form


# def signin(request):
#     if request.method == 'GET':
#         return render(request, 'base/signin.html', {
#             'form': AuthenticationForm
#         })
#     else:
#         user = authenticate(
#             request, username=request.POST['username'], password=request.POST['password'])
#         if user is None:
#             return render(request, 'base/signin.html', {
#                 'form': AuthenticationForm,
#                 'error': 'Usuario o password incorrecto'
#             })
#         else:
#             login(request, user)

#             if Contact.objects.filter(user=request.user).exists():
#                 return redirect('dashboard')
#             else:
#                 return redirect('contact')


# def signout(request):
#     logout(request)
#     return redirect('home')
