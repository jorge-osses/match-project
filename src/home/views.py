from django.shortcuts import render, HttpResponse
from home import varyfun as varyfunhome
from base import varyfun as varyfunbase
from register import varyfun as varyfunregister

titlehead = 'Match - Home'
# Create your views here.

"""
def home(request):
    return HttpResponse(varyfunbase.head1+titlehead+varyfunbase.head2+varyfunbase.navbar+varyfunhome.body+varyfunbase.footer)
"""


def home(request):
    return render(request, "base/home.html")


def about(request):
    return render(request, "base/about.html")


def faq(request):
    return render(request, "base/faq.html")


def register(request):
    return HttpResponse(varyfunbase.head1+titlehead+varyfunbase.head2+varyfunbase.navbar+varyfunregister.body+varyfunbase.footer)
