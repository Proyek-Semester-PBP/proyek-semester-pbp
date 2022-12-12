from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from profilepage.models import Profile
from recycle.models import RecycleHistory
from django.core import serializers


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
                "name": user1.name,
                "email": user1.email,
                "github": user1.github,
                "instagram": user1.instagram,
                "twitter": user1.twitter,
                "facebook": user1.facebook,
                "point": user1.point,
                "weight": user1.weight,
                "profpic": user1.profpic,
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

   


def NewProfile(user):
    try:
        temp = Profile.objects.get(user = user) 
        return temp
    except Profile.DoesNotExist:
        url = "https://img.freepik.com/free-vector/cute-cow-surprised-cartoon-vector-icon-illustration-animal-nature-icon-concept-isolated-premium-vector-flat-cartoon-style_138676-3874.jpg?w=360"
        RecycleHistory.objects.create(user = user, name = user, date = "-", weight = 0, point = 0, location = "-", is_pickup = False, description = "-")
        return Profile.objects.create(user=user, name="-", email="-", mobile="-", github="-", instagram="-", twitter="-", facebook="-", point = 0, weight = 0, profpic = url)