from asyncio.log import logger
import http
from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from .models import Profile
from django.http import HttpResponseRedirect, JsonResponse
from home.models import User
from django.core.files.storage import FileSystemStorage
from recycle.models import RecycleHistory
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def show_profile(request):
    user = request.user
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        request_type = request.POST.get("request_type")
        if request_type == "edit_profile":
            name = request.POST.get("name")
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            github = request.POST.get("github")
            instagram = request.POST.get("instagram")
            twitter = request.POST.get("twitter")
            facebook = request.POST.get("facebook")   
            Profile.objects.filter(user = user).update(name = name, email = email, mobile = mobile, github = github, instagram = instagram, twitter = twitter, facebook = facebook)
        
    elif request.method == 'POST' and request.FILES.get('image') != None:
        myimage = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myimage.name, myimage)
        url = fs.url(filename)
        temp = Profile.objects.get(user=user)
        temp.profpic = url
        temp.save()


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
        'weight': data_user1.weight,
        'profpic': data_user1.profpic,
    }
    return render(request, "profile.html", context)
    
       


