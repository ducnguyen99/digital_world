from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout 
# Create your views here.
def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        print(request.body)
        print(request)
        form = CreateUserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('product')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def login_page(request):
    if request.method == 'POST':
        print(request.body)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('product')
    context = {}
    return render(request, 'login.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')
