from django.shortcuts import render

# Create your views here.
def cart(request):
    context = {}
    return render(request, 'cartt.html', context)

def login(request):
    context = {}
    return render(request, 'login.html', context)