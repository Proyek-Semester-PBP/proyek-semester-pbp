from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from shopping.models import RecommendedItem, RecommendedVendor
from random import randint

# Create your views here.
def show_shop(request):
    return render(request, "shop.html")

def show_item_json(request):
    itemAmount = RecommendedItem.objects.all().count()
    itemData = RecommendedItem.objects.filter(pk__in=generate_pk(6, itemAmount))
    return HttpResponse(serializers.serialize("json", itemData), content_type="application/json")

def show_vendor_json(request):
    vendorAmount = RecommendedVendor.objects.all().count()
    vendorData = RecommendedVendor.objects.filter(pk__in=generate_pk(3, vendorAmount))
    return HttpResponse(serializers.serialize("json", vendorData), content_type="application/json")

def generate_pk(amount, max):
    pk_list = []

    while len(pk_list) != amount:
        pk = randint(1,max)
        if pk not in pk_list:
            pk_list.append(pk)

    return pk_list