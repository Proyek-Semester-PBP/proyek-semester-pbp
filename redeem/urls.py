from django.urls import path
from redeem.views import show_redeem
from redeem.views import show_json

app_name = 'redeem'

urlpatterns = [
    path('', show_redeem, name='show_redeem'),
    path('json/', show_json, name='show_json'),
]