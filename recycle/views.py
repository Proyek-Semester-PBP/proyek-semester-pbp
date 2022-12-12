from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from recycle.models import RecycleHistory
from recycle.forms import PickUpForm
from recycle.forms import DropOffForm
from django.contrib.auth.decorators import login_required
from profilepage.models import Profile
from django.views.decorators.csrf import csrf_exempt

def show_dumb(request):
    dropoff_form = DropOffForm()
    pickup_form = PickUpForm()
    context = {
        "dropoff_form" : dropoff_form,
        "pickup_form" : pickup_form
    }
    return render(request, "recycle2.html", context)


# Create your views here.
def show_recycle(request):
    dropoff_form = DropOffForm()
    pickup_form = PickUpForm()
    context = {
        "dropoff_form" : dropoff_form,
        "pickup_form" : pickup_form
    }
    return render(request, "recycle.html", context)

@login_required(login_url='/login/')
def create_pickup(request):
    if request.method == 'POST':
        pickup_form = PickUpForm(request.POST)
    else:
        pickup_form = PickUpForm()
    context = {"pickup_form" : pickup_form}
    return render(request, 'pickup_form.html', context)

@login_required(login_url='/login/')
def create_dropoff(request):
    if request.method == 'POST':
        dropoff_form = DropOffForm(request.POST)
    else:
        dropoff_form = DropOffForm()
    context = {"dropoff_form" : dropoff_form}
    return render(request, 'dropoff_form.html', context)

def show_json(request):
    data = RecycleHistory.objects.get(user=request.user).all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def add_history_flutter(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        weight = request.POST.get('weight')
        description = request.POST.get('description')
        is_pickup = request.POST.get('is_pickup')
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
        return JsonResponse({"instance":"Project created"}, status=200)
    else:
        return JsonResponse({"Failed"}, status=404)

def add_history(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        weight = request.POST.get('weight')
        description = request.POST.get('description')
        if (request.POST.get('type') == "pickup"):
            location = request.POST.get('detail') + ", " + request.POST.get('subdistrict') + ", " +  \
                        request.POST.get('city') + ", " + request.POST.get('region') + " - " + request.POST.get('zip_code')
            is_pickup = True
        else:
            location = request.POST.get('location')
            is_pickup = False
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
        temp = Profile.objects.get(user=request.user)
        temp.weight += (int(weight))
        temp.point += (int(weight) * 5)
        temp.save()
        return HttpResponse('')
    return redirect('recycle:show_recycle')
