from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signup(request):
    if request.method == 'POST':
        """
        username = request.POST['username']
        firstname = request.POST['firstname']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create(username=username, first_name=firstname, email=email, password=password)
        user.save()
        """
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'accounts/signup.html', context={'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            redirect('home')

    return render(request, 'accounts/login.html')


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        redirect('home')
    return render(request, 'accounts/logout.html')


