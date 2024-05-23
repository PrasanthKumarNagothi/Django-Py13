from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def homepage(request):
    # return HttpResponse('Welcome to Backend with django')
    students = [
        {
            "name": "Prakash",
            "age": 22,
            "number": 9876554321,
            "marks": 35
        },
        {
            "name": "Sarath",
            "age": 23,
            "number": 87483378437,
            "marks": 34
        },
        {
            "name": "Yashwanth",
            "age": 24,
            "number": 983748378,
            "marks": 60
        }
    ]

    return render(request, 'home.html', {'students': students})
