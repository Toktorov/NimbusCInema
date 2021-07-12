from django.shortcuts import render, redirect
from django.contrib import messages
from apps.users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        nickname = request.POST.get('nickname')
        image = request.FILES.get('image')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(image)
        if password1 == password2:
            try:
                user = User.objects.create(username=username)
                user.set_password(password1)
                user.save()
                profile = Profile.objects.create(user=user, nickname=nickname, image=image)
                user = authenticate(username=username, password=password1)
                login(request, user)
                return redirect('index')
            except:
                messages.error(request, 'Not correct some value')
        else:
            messages.error(request, 'Not correct password')
    return render(request, 'account/signup.html')


def login_user(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.get(username=username)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        except:
            messages.error(request, 'Not correct login or password')
    return render(request, 'account/login.html')

def profile(request, username):
    users = User.objects.get(username=username)
    context = {
       "user": users,
    }
    return render(request, 'account/profile.html', context)