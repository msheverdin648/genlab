from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect 



def index(request):
    return render(request, 'base.html', {})
