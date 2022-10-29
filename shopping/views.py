from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from shopping.models import RecommendedItem, RecommendedVendor

# Create your views here.
def show_shop(request):
    return render(request, "shop.html")

def show_item_json(request):
    itemData = RecommendedItem.objects.order_by('?')[:6]
    return HttpResponse(serializers.serialize("json", itemData), content_type="application/json")

def show_vendor_json(request):
    vendorData = RecommendedVendor.objects.order_by('?')[:3]
    return HttpResponse(serializers.serialize("json", vendorData), content_type="application/json")