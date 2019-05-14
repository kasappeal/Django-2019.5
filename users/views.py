from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout

from users.forms import LoginForm


def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, 'Usuario/contraseña incorrectos')
            else:
                django_login(request, user)
                url = request.GET.get('next', 'home')
                return redirect(url)
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'users/login.html', context)


def logout(request):
    django_logout(request)
    return redirect('login')
