from django.shortcuts import render, HttpResponse
from register import varyfun as varyfunregister
from base import varyfun as varyfunbase

titlehead = 'Match - FAQ'
# Create your views here.


def register(request):
 
    return HttpResponse(varyfunbase.head1+titlehead+varyfunbase.head2+varyfunbase.navbar+varyfunregister.body+varyfunbase.footer)



