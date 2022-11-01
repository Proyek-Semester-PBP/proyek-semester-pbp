from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import User
from profilepage.models import Profile

# Create your views here.
def show_homepage(request):
    return render(request, "home.html")

@login_required(login_url='/home/login/')
def show_home_loggedin(request):
    return render(request, "home_loggedin.html")

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            NewProfile(user)
            response = HttpResponseRedirect(reverse('home:show_home_loggedin'))
            return response

    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('home:show_homepage'))
    return response

def NewProfile(user):
    try:
        temp = Profile.objects.get(user = user) 
    except Profile.DoesNotExist:
        url = "https://img.freepik.com/free-vector/cute-cow-surprised-cartoon-vector-icon-illustration-animal-nature-icon-concept-isolated-premium-vector-flat-cartoon-style_138676-3874.jpg?w=360"
        return Profile.objects.create(user=user, name="-", email="-", mobile="-", github="-", instagram="-", twitter="-", facebook="-", point = 0, weight = 0, profpic = url)
        
    