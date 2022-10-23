from django.urls import path
from redeem.views import show_redeem

app_name = 'redeem'

urlpatterns = [
    path('', show_redeem, name='show_redeem'),
]