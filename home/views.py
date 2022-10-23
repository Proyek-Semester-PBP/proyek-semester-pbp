from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def show_homepage(request):
    return render(request, "home.html")

def login_user(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def logout_user(request):
    return HttpResponseRedirect(reverse('home:show_homepage'))