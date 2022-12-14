from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from profilepage.models import Profile
from recycle.models import RecycleHistory
from django.core import serializers
from django.core.files.storage import FileSystemStorage


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            temp = NewProfile(user)
            user1 = Profile.objects.get(user = request.user)
            # data = serializers.serialize('json', user1)
            # Redirect to a success page. Tests
            return JsonResponse({
            "status": True,
            "message": "Successfully Logged In!",
            # Insert any extra data if you want to pass data to Flutter
            "data": {
                "user": request.user.username,
                "name": user1.name,
                "email": user1.email,
                "mobile": user1.mobile,
                "github": user1.github,
                "instagram": user1.instagram,
                "twitter": user1.twitter,
                "facebook": user1.facebook,
                "point": user1.point,
                "weight": user1.weight,
                "profpic": user1.profpic.path,
                "email": user1.email,   
            }
            

            }, status=200)
        else:
            return JsonResponse({
            "status": False,
            "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
        "status": False,
        "message": "Failed to Login, check your email/password."
        }, status=401)

@csrf_exempt
def logout_user(request):
    logout(request)
    return JsonResponse({
        'status': True,
        'message': 'Successfully Logged Out!',
    }, status=200)

def NewProfile(user):
    try:
        temp = Profile.objects.get(user = user) 
        return temp
    except Profile.DoesNotExist:
        url = "https://img.freepik.com/free-vector/cute-cow-surprised-cartoon-vector-icon-illustration-animal-nature-icon-concept-isolated-premium-vector-flat-cartoon-style_138676-3874.jpg?w=360"
        RecycleHistory.objects.create(user = user, name = user, date = "-", weight = 0, point = 0, location = "-", is_pickup = False, description = "-")
        return Profile.objects.create(user=user, name="-", email="-", mobile="-", github="-", instagram="-", twitter="-", facebook="-", point = 0, weight = 0, profpic = url)

@csrf_exempt
def show_profile(request):
    user = request.user
    name = request.POST.get("name")
    email = request.POST.get("email")
    mobile = request.POST.get("mobile")
    github = request.POST.get("github")
    instagram = request.POST.get("instagram")
    twitter = request.POST.get("twitter")
    facebook = request.POST.get("facebook")   
    Profile.objects.filter(user = user).update(name = name, email = email, mobile = mobile, github = github, instagram = instagram, twitter = twitter, facebook = facebook)
        
    # if request.method == 'POST' and request.FILES.get('image') != None:
    #     myimage = request.FILES['image']
    #     fs = FileSystemStorage()
    #     filename = fs.save(myimage.name, myimage)
    #     url = fs.url(filename)
    #     temp = Profile.objects.get(user=user)
    #     temp.profpic = url
    #     temp.save()
    
    return JsonResponse({
        "status": True,
        "message": "Success updating profile",
    }, status=200)