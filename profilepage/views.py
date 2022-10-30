from asyncio.log import logger
import http
from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from .models import Profile
from django.http import HttpResponseRedirect
from home.models import User

# Create your views here.
def show_profile(request):
    user = request.user
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        github = request.POST.get("github")
        instagram = request.POST.get("instagram")
        twitter = request.POST.get("twitter")
        facebook = request.POST.get("facebook")
        Profile.objects.filter(user = user).update(name = name, email = email, mobile = mobile, github = github, instagram = instagram, twitter = twitter, facebook = facebook)
    
    data_user1 = Profile.objects.get(user = user)
    context = {
        'user': user,
        'name': data_user1.name,
        'email': data_user1.email,
        'mobile': data_user1.mobile,
        'github': data_user1.github,
        'instagram': data_user1.instagram,
        'twitter': data_user1.twitter,
        'facebook': data_user1.facebook,
        'point': data_user1.point,
        'plastic': data_user1.plastics
    }
    return render(request, "profile.html", context)
    
       


