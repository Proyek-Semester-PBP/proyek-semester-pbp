from django.urls import path
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name = 'login'),
    path('update/', show_profile, name = 'update_profile'),
]