from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from news.models import NewsData
from news.forms import FormPage
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='/news/login/')
def show_news(request):
    data_news = NewsData.objects.all()
    context = {
        'list_data' : data_news
    }
    return render(request, "news.html", context)

# @login_required(login_url='/news/login/')
def show_json(request):
    data_json = NewsData.objects.all()
    return HttpResponse(serializers.serialize("json", data_json), content_type="application/json")

# @login_required(login_url='/news/login/')
def show_json_by_id(request,id):
    data_json_id = NewsData.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_json_id), content_type="application/json")

# @login_required(login_url='/news/login/')
def halaman_form(request):
    if request.method == 'POST':
        form = FormPage(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user=request.user
            task.date=request.date
            task.save()
            return redirect("news:show_news")

    form = FormPage()
    context = {'form':form}
    return render(request, "task.html", context)