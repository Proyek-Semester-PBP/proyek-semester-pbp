from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='/login/')
def show_bookmark_json(request):
    bookmarkData = RecommendedItem.objects.filter(bookmarks=request.user)
    return HttpResponse(serializers.serialize("json", bookmarkData), content_type="application/json")

@login_required(login_url='/login/')
def bookmark_item(request, id):
    if request.method == 'POST':
        bookmarkedItem = RecommendedItem.objects.filter(pk=id).get()
        bookmarkedItem.bookmarks.add(request.user)
        bookmarkedItem.save()
        return HttpResponse("Item Bookmarked", status=201)

    return HttpResponseNotFound()

@login_required(login_url='/login/')
def remove_bookmark(request, id):
    if request.method == 'DELETE':
        bookmarkedItem = RecommendedItem.objects.filter(pk=id).get()
        bookmarkedItem.bookmarks.remove(request.user)
        return HttpResponse("Bookmark Removed", status=204)
    
    return HttpResponseNotFound()