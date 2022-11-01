from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from news.models import NewsData
# Create your views here.
def show_news(request):
    return render(request, "news.html")

def show_json(request):
    data_json = NewsData.objects.all()
    return HttpResponse(serializers.serialize("json", data_json), content_type="application/json")

def show_json_by_id(request,id):
    data_json_id = NewsData.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_json_id), content_type="application/json")