from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse('Welcome to Backend with django')
    return render(request, 'home.html')
