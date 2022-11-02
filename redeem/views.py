from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from redeem.models import Voucher
from django.core import serializers
from django.http.response import JsonResponse, HttpResponse

# Create your views here.
def show_redeem(request):
    return render(request, "redeem.html")

def show_json(request):
    voucher = Voucher.objects.all()
    return HttpResponse(serializers.serialize('json', voucher), content_type='application/json')
