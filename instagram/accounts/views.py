from django.shortcuts import render
from . models import Users

# Create your views here.


def register(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        username = request.POST['username']
        password = request.POST['password']

        Users.objects.create(
            firstName=firstName,
            lastName=lastName,
            username=username,
            password=password
        )

    return render(request, 'accounts/register.html')
