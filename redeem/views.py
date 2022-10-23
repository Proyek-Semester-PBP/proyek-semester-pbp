from django.shortcuts import render

# Create your views here.
def show_redeem(request):
    return render(request, "redeem.html")