from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . models import UserDetails
# Create your views here.


def register(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        dob = request.POST['dob']
        gender = request.POST['gender']
        mobile = request.POST['mobile']

        user = User.objects.create_user(
            first_name=firstName,
            last_name=lastName,
            username=username,
            password=password,
            email=email
        )

        UserDetails.objects.create(
            gender=gender,
            dob=dob,
            mobile=mobile,
            user_id=user.id
        )

    return render(request, 'accounts/register.html')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')

    return render(request, 'accounts/login.html')
