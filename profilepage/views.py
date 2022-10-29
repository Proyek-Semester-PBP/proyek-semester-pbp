from asyncio.log import logger
from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from .models import Profile
from django.http import HttpResponseRedirect
from home.models import User

# Create your views here.
def show_profile(request):
    user = request.user
    data_user1 = Profile.objects.get(user = user)
    context = {
        'user': request.user,
        'name': data_user1.name,
        'email': data_user1.email,
        'mobile': data_user1.mobile,
        'github': data_user1.github,
        'instagram': data_user1.instagram,
        'twitter': data_user1.twitter,
        'facebook': data_user1.facebook,
    }
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        github = request.POST.get("github")
        instagram = request.POST.get("instagram")
        twitter = request.POST.get("twitter")
        facebook = request.POST.get("facebook")
    
        i = Profile.objects.filter(user = user).update(name = name, email = email, mobile = mobile, github = github, instagram = instagram, twitter = twitter, facebook = facebook)
    
        return render(request, "profile.html", context)
    else:
        return render(request, "profile.html", context)

    


def editProfile(user, name, email, mobile, github, instagram, twitter, facebook):
    return Profile.objects.create(user=user, name=name, email=email, mobile=mobile, github=github, instagram=instagram, twitter=twitter, facebook=facebook )

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'