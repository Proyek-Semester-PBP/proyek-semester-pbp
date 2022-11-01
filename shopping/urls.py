from django.urls import path
from shopping.views import show_shop, show_item_json, show_vendor_json, show_bookmark_json
from shopping.views import bookmark_item, remove_bookmark

app_name = 'shopping'

urlpatterns = [
    path('', show_shop, name='show_shop'),
    path('json-item/', show_item_json, name='show_item_json'),
    path('json-vendor/', show_vendor_json, name='show_vendor_json'),
    path('json-bookmark/', show_bookmark_json, name='show_bookmark_json'),
    path('bookmark/<int:id>', bookmark_item, name='bookmark_item'),
    path('remove-bookmark/<int:id>', remove_bookmark, name='remove_bookmark'),
]