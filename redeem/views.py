from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from redeem.models import Voucher
from redeem.models import Newvoucher
from django.core import serializers
from django.contrib.auth.decorators import login_required
from redeem.forms import VoucherForm
from django.http.response import JsonResponse, HttpResponse
from django.http.response import HttpResponse

# Create your views here.
def show_redeem(request):
    return render(request, "redeem.html")

def show_json(request):
    voucher = Voucher.objects.all()
    return HttpResponse(serializers.serialize('json', voucher), content_type='application/json')

@login_required(login_url='/login/') 
def request_voucher(request):
    form = VoucherForm()
    if request.method == "POST":
        form = VoucherForm(request.POST)
        if form.is_valid():
            form.save()

    return HttpResponse(status=200)


