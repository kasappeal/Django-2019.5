from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout


def login(request):
    if request.method == 'POST':
        username = request.POST['usr']
        password = request.POST['pwd']
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Usuario/contraseña incorrectos')
        else:
            django_login(request, user)
            return redirect('home')
    return render(request, 'users/login.html')


def logout(request):
    django_logout(request)
    return redirect('login')
