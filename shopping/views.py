from django.shortcuts import render

# Create your views here.
def show_shop(request):
    return render(request, "shop.html")