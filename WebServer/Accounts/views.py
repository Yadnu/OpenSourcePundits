from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CreateUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/', {'user_name': username})


    return render(request, 'login.html')


@login_required(login_url='/login')
def logout_page(request):
    logout(request)
    return redirect('/login')