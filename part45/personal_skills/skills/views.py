from django.shortcuts import render, redirect
from .models import Skills
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def index(request):
    prog = Skills.objects.all()
    return render(request, 'skills/index.html', {'prog': prog})


def signupuser(request):
    if request.method == "GET":
        return render(request, 'skills/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'skills/signupuser.html', {
                    'form': UserCreationForm(),
                    'error': 'Такое имя пользователя уже существует. Создайте другое'})
        else:
            return render(request, 'skills/signupuser.html', {
                'form': UserCreationForm(),
                'error': 'Пароли не совпадают'})


@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'skills/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'skills/loginuser.html', {
                'form': AuthenticationForm(),
                'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('index')
