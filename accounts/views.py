from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import signupForm


# Create your views here.
def signup(request):
    form = signupForm()
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('login_user')
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


