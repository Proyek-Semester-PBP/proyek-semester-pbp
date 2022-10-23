from django.shortcuts import render

# Create your views here.
def show_recycle(request):
    return render(request, "recycle.html")