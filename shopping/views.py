from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.contrib.auth.decorators import login_required
from shopping.models import RecommendedItem, RecommendedVendor, Review
from shopping.forms import ReviewForm

# Create your views here.
def show_shop(request):
    return render(request, "shop.html")

def show_item_json(request):
    item_data = RecommendedItem.objects.order_by('?')[:6]
    return HttpResponse(serializers.serialize("json", item_data), content_type="application/json")

def show_vendor_json(request):
    vendor_data = RecommendedVendor.objects.order_by('?')[:3]
    return HttpResponse(serializers.serialize("json", vendor_data), content_type="application/json")

@login_required(login_url='/login/')
def show_bookmark_json(request):
    bookmark_data = RecommendedItem.objects.filter(bookmarks=request.user)
    return HttpResponse(serializers.serialize("json", bookmark_data), content_type="application/json")

def show_review_json(request):
    review_data = Review.objects.order_by('?')[:1]
    return HttpResponse(serializers.serialize("json", review_data), content_type="application/json")

@login_required(login_url='/login/')
def bookmark_item(request, id):
    if request.method == 'POST':
        bookmarked_item = RecommendedItem.objects.filter(pk=id).get()
        bookmarked_item.bookmarks.add(request.user)
        bookmarked_item.save()
        return HttpResponse("Item Bookmarked", status=201)

    return HttpResponseNotFound()

@login_required(login_url='/login/')
def remove_bookmark(request, id):
    if request.method == 'DELETE':
        bookmarked_item = RecommendedItem.objects.filter(pk=id).get()
        bookmarked_item.bookmarks.remove(request.user)
        return HttpResponse("Bookmark Removed", status=204)
    
    return HttpResponseNotFound()

@login_required(login_url='/login/')
def make_review(request, id):
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_data = form.save(commit=False)
            review_data.user = request.user.get_username()
            review_data.item = RecommendedItem.objects.filter(pk=id).get().name
            review_data.save()
            return HttpResponse("Review Made", status=201)

    return HttpResponseNotFound()