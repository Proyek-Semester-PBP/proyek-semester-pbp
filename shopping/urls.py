from django.urls import path
from shopping.views import show_shop, show_item_json, show_vendor_json

app_name = 'shopping'

urlpatterns = [
    path('', show_shop, name='show_shop'),
    path('json-item/', show_item_json, name='show_item_json'),
    path('json-vendor/', show_vendor_json, name='show_vendor_json'),
]