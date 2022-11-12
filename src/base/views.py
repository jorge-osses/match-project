from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'base/home.html'

    def home(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'title': "Match"
        })


class FaqView(TemplateView):
    template_name = "base/faq.html"


class AboutView(TemplateView):
    template_name = "base/about.html"


class LoginView(TemplateView):
    template_name = "base/login.html"
