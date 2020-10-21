from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout 

from django.http import HttpResponse, HttpResponseRedirect
import json
from products.utils import *
from .decorators import *
# Create your views here.

@unauthenticated_user
def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('product')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next')

        user = authenticate(request, username=username, password=password)
        print('before if')
        if user is not None:
            login(request, user)
            if bool(next_url):
               create_cart(request)
               return redirect(next_url)
            else:
                print('next url is false')
                create_cart(request) 
                return redirect('product')
    context = {}
    return render(request, 'login.html', context)

def logout_page(request):
    logout(request)
    return redirect('product')
