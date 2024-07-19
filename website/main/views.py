from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required

from .forms import PostForm
from .models import Post


@login_required(login_url='/login')
def home(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        post_id = request.POST.get("post-id")
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()
    return render(request, 'main/home.html', {'posts': posts})


@ login_required(login_url='/login')
@permission_required("main.add_post", raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)  # Filled form if POST request
        if form.is_valid():
            post = form.save(commit=False)  # Do not save the form yet in  DB
            post.author = request.user
            post.save()
            return redirect('/home')
    else:
        form = PostForm()  # Empty form if GET request
    return render(request, 'main/create_post.html', {'form': form})


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
