from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Redirects to login page if user is not logged in
@login_required(login_url='/login')
def home(request):
    return render(request, 'main/home.html')


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form': form})


def log_out(request):
    logout(request)
    # TODO maybe this is redundant with the settings.py REDIRECT_URL setting
    return redirect('/login')
