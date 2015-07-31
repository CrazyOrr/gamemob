from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login


# Create your views here.
def register_succeed(request):
    template_name = 'registration/register_succeed.html'
    return render(request, template_name)

