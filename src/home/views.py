from django.shortcuts import render, HttpResponse
from home import varyfun as varyfunhome
from base import varyfun as varyfunbase

titlehead = 'Match - Home'
# Create your views here.


def home(request):
    
    return HttpResponse(varyfunbase.head1+titlehead+varyfunbase.head2+varyfunbase.navbar+varyfunhome.body+varyfunbase.footer)


