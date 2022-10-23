from django.urls import path
from home.views import show_homepage

app_name = 'home'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
]