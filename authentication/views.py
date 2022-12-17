from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from home.forms import CustomUserCreationForm
from profilepage.models import Profile
from recycle.models import RecycleHistory
from django.core import serializers
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User  


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
def register(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    password1 = request.POST.get("password1")
    password2 = request.POST.get("password2")

    if not username or not email or not password1 or not password2:
        return JsonResponse({
            "status": False,
            "message": "Missing a field!"
            }, status=401)

    new = User.objects.filter(username = username)
    if new.count():
        return JsonResponse({'success': False, 'message': 'User already exists'}, status=400)
    
    new2 = User.objects.filter(email = email)
    if new2.count():
        return JsonResponse({'success': False, 'message': 'Email already exists'}, status=400)
    
    if password1 and password2 and password1 != password2: 
        return JsonResponse({'success': False, 'message': "Password don't match"}, status=400)
    
    user = User.objects.create_user(username, email, password1)
    return JsonResponse({'success': True, 'message': 'Successfully created a new account'}, status=200)



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
        return Profile.objects.create(user=user, name="-", email= user.email, mobile="-", github="-", instagram="-", twitter="-", facebook="-", point = 0, weight = 0, profpic = url)

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

@csrf_exempt
def addPoint(request):
    user = request.user
    temp = Profile.objects.get(user = user)
    weights = request.POST.get("weights")
    temp.weight += int(weights)
    temp.point += (int(weights)*5)

    name = request.POST.get("name")
    description = request.POST.get("description")
    is_pickup = request.POST.get("is_pickup")
    if is_pickup == 'true':
        is_pickup = True
    else:
        is_pickup = False
    location = request.POST.get("location")
    history = RecycleHistory(
        user=user,
        name=name,
        weight=int(weights),
        point=int(weights)*5,
        location=location,
        is_pickup=is_pickup, 
        description=description,
    )
    history.save()
    temp.save()
    
    return JsonResponse({
        "status": True,
        "message": "Success updating profile",
    }, status=200)

@csrf_exempt
def add_history_flutter(request):
    name = request.POST.get('name')
    weight = request.POST.get('weight')
    description = request.POST.get('description')
    is_pickup = request.POST.get('is_pickup')
    if is_pickup == 'true':
        is_pickup = True
    else:
        is_pickup = False
    location = request.POST.get('location')
    new_history = RecycleHistory(
            user=request.user,
            name=name,
            weight=int(weight),
            point=int(weight)*5,
            location=location,
            is_pickup=is_pickup, 
            description=description,
    )
    new_history.save()
    return JsonResponse({
            "status": True,
            "message": "Success",
    }, status=200)

@csrf_exempt
def redeem(request):
    user = request.user
    point = request.POST.get("points")
    temp = Profile.objects.get(user = user)
    if int(point) > temp.point:
         return JsonResponse({
        "status": False,
        "message": "You don't have enough points to redeem!",
    }, status=400)
    else:
        temp.point -= int(point)
        temp.save()
        return JsonResponse({
        "status": True,
        "message": "Successfuly redeem the item!",
    }, status=200)

    
