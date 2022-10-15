from django.shortcuts import render, HttpResponse
from home import varyfun, home2
from base import varyfun as varyfunbase

titlehead = 'Home'
# Create your views here.


def home(request):
    # return HttpResponse(home2.head+home2.body)
    return HttpResponse(varyfunbase.head1+titlehead+varyfunbase.head2)


