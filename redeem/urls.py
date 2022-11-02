from django.urls import path
from redeem.views import show_redeem
from redeem.views import show_json, request_voucher

app_name = 'redeem'

urlpatterns = [
    path('', show_redeem, name='show_redeem'),
    path('json/', show_json, name='show_json'),
    path('submit/', request_voucher, name ='request_voucher')
]