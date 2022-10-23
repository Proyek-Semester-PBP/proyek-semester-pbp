from django.urls import path
from shopping.views import show_shop

app_name = 'shopping'

urlpatterns = [
    path('', show_shop, name='show_shop'),
]